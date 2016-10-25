import os
import click
import yaml
import psycopg2
import sys
import logging
import user
import json
import pandas as pd

from db import DatabaseManager
from access import AccessManager
from relation import RelationManager
from version import VersionManager
from metadata import MetadataManager
from user_control import UserManager

from orpheus_exceptions import BadStateError, NotImplementedError, BadParametersError

class Context():
    def __init__(self):
        self.config_path = 'config.yaml'
        try:
            with open(self.config_path, 'r') as f:
                self.config = yaml.load(f)
        except (IOError, KeyError):
            raise BadStateError("config.yaml file not found or data not clean, abort")
            return
        except: # unknown error
            raise BadStateError("unknown error during loding config file, abort")
            return


@click.group()
@click.pass_context
def cli(ctx):
    try:
        ctx.obj = Context().config
        user_obj = UserManager.get_current_state()
        for key in user_obj:
            ctx.obj[key] = user_obj[key]
        if not ctx.obj or not ctx.obj['user'] or not ctx.obj['database']:
            click.secho("No session in use, please call config first", fg='red')
    except Exception as e:
        click.secho(str(e), fg='red')

@cli.command()
@click.option('--user', prompt='Enter user name', help='Specify the user name that you want to configure to.')
@click.option('--password', prompt=True, hide_input=True, help='Specify the password.')
@click.pass_context
def config(ctx, user, password):
    newctx = ctx.obj # default
    try:
        if UserManager.verify_credential(user, password):
            from encryption import EncryptionTool
            newctx['user'] = user
            newctx['passphrase'] = EncryptionTool.passphrase_hash(password)
            UserManager.write_current_state(newctx) # pass down to user manager
            click.echo('logged in as %s' % user)
    except Exception as e:
        click.secho(str(e), fg='red')


@cli.command()
@click.option('--user', prompt='Enter user name', help='Specify the user name that you want to create.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='Specify the password that you want to use.')
@click.pass_context
def create_user(ctx, user, password):
    # check this user has permission to create new user or not
    # create user in UserManager
    click.echo("creating user into %s" % ctx.obj['database'])
    try:
        UserManager.create_user(user, password)
        DatabaseManager.create_user(user, password, ctx.obj['database']) #TODO: need revise
        click.echo('User created.')
    except Exception as e:
        click.secho(str(e), fg='red')
    
@cli.command()
@click.option('--database', '-d', help='Specify the database that you want to use without changing host and port')
@click.pass_context
def db(ctx, database):
    # TODO: check permission?
    print ctx.obj
    if database:
        ctx.obj['database'] = database
        UserManager.write_current_state(ctx.obj) # write to persisent store
    click.echo('using: %s' % ctx.obj['database'])

@cli.command()
@click.pass_context
def whoami(ctx):
    click.echo('logged in as: %s' % ctx.obj['user'])

@cli.command()
@click.argument('input', type=click.Path(exists=True))
@click.argument('dataset')
@click.option('--schema', '-s', help='Specify the schema (existed table) of this input data')
@click.option('--header', '-h', is_flag=True, help="If set, the first line of the input file should be header")
@click.pass_context
def init(ctx, input, dataset, schema, header):
    # TODO: add header support
    # By default, we connect to the database specified in the -config- command earlier

    # Two cases need to be taken care of:
    # 1.add version control on an outside file
    #    1.1 Load a csv or other format of the file into DB
    #    1.2 Schema
    # 2.add version control on a existing table in DB
    try:
        conn = DatabaseManager(ctx.obj)
        rel = RelationManager(conn)

        attribute_name , _ = rel.get_datatable_attribute(schema)
    except Exception as e:
        click.secho(str(e), fg='red')
        return

    # at this point, we have a valid conn obj and rel obj
    try:
        conn.create_dataset(input, dataset, schema=schema, attributes=attribute_name)
        # get all rids in list
        lis_rid = rel.select_all_rid(dataset + '_datatable')

        # init version info
        version = VersionManager(conn)
        version.init_version_graph_dataset(dataset, lis_rid)
        version.init_index_table_dataset(dataset, lis_rid)

        click.echo("%s create successful" % dataset)

    except Exception as e:
        # revert back to the state before create
        conn.drop_dataset(dataset)
        click.secho(str(e), fg='red')
    # TODO: What about schema? Automation or specified by user?

@cli.command()
@click.argument('dataset')
@click.pass_context
def drop(ctx, dataset):
    try:
        conn = DatabaseManager(ctx.obj)
        click.echo("dropping dataset %s" % dataset)
        conn.drop_dataset(dataset)
    except Exception as e:
        click.secho(str(e), fg='red')

@cli.command()
@click.option('--dataset', '-d', help='Specify the dataset to show')
@click.option('--table_name', '-t', help='Specify the table to show')
@click.pass_context
def ls(ctx, dataset, table_name):
    # if no dataset specified, show the list of dataset the current user owns
    try:
        conn = DatabaseManager(ctx.obj)
        if not dataset:
            click.echo("\n".join(conn.list_dataset()))
        else:
            click.echo(conn.show_dataset(dataset))

    # when showing dataset, chop off rid
    except Exception as e:
        click.secho(str(e), fg='red')


@cli.command()
@click.argument('dataset')
@click.option('--vlist', '-v', multiple=True, required=True, help='Specify version you want to clone, use multiple -v for multiple version checkout')
@click.option('--to_table', '-t', help='Specify the table name to checkout to.')
@click.option('--to_file', '-f', help='Specify the location of file')
@click.option('--delimeters', '-d', default=',', help='Specify the delimeter used for checkout file')
@click.option('--header', '-h', is_flag=True, help="If set, the first line of checkout file will be the header")
@click.option('--ignore', '-i', is_flag=True, help='If set, clone versions into table will ignore duplicated key')
@click.pass_context
def clone(ctx, dataset, vlist, to_table, to_file, delimeters, header, ignore):
    # check ctx.obj has permission or not
    if not to_table and not to_file:
        raise BadParametersError("Need a destination, either a table or a file")
        return

    try:
        conn = DatabaseManager(ctx.obj)
        relation = RelationManager(conn)
    except Exception as e:
        click.secho(str(e), fg='red')
        return

    abs_path = ctx.obj['orpheus_home'] + to_file if to_file and to_file[0] != '/' else to_file

    try:
        metadata = MetadataManager(ctx.obj)
        meta_obj = metadata.load_meta()
        datatable = dataset + "_datatable"
        indextable = dataset + "_indexTbl"

        relation.checkout(vlist, datatable, indextable, to_table=to_table, to_file=abs_path, delimeters=delimeters, header=header, ignore=ignore)
        # update meta info
        AccessManager.grant_access(to_table, conn.user)
        metadata.update(to_table, abs_path, dataset, vlist, meta_obj)
        metadata.commit_meta(meta_obj)
        if to_table:
            click.echo("Table %s has been cloned from version %s" % (to_table, ",".join(vlist)))
        if to_file:
            click.echo("File %s has been cloned from version %s" % (to_file, ",".join(vlist)))
    except Exception as e:
        if to_table:
            relation.drop_table(to_table)
        if to_file:
            pass # delete the file
        click.secho(str(e), fg='red')

    

@cli.command()
@click.option('--msg','-m', help='Commit message', required = True)
@click.option('--table_name','-t', help='The table to be committed') # changed to optional later
@click.option('--file_name', '-f', help='The file to be committed', type=click.Path(exists=True))
@click.option('--schema', '-s', help='Specify the schema (existed table) of this input data')
@click.option('--delimeters', '-d', default=',', help='Specify the delimeter used for checkout file')
@click.option('--header', '-h', is_flag=True, help="If set, the first line of checkout file will be the header")
@click.pass_context
def commit(ctx, msg, table_name, file_name, schema, delimeters, header):

    # sanity check
    if not table_name and not file_name:
        raise BadParametersError("Need a source, either a table or a file")
        return

    if table_name and file_name:
        raise NotImplementedError("Supporting both file and table commit is not implemented")
        return

    try:
        conn = DatabaseManager(ctx.obj)
        relation = RelationManager(conn)
        metadata = MetadataManager(conn)
        version = VersionManager(conn)
    except Exception as e:
        click.secho(str(e), fg='red')

    if table_name and not relation.check_table_exists(table_name):
        click.secho(str(relation.RelationNotExistError(table_name)), fg='red')
        return

    # load parent information about the table
    # We need to get the derivation information of the committed table;
    # Otherwise, in the multitable scenario, we do not know which datatable/version_graph/index_table
    # that we need to update information.
    try:
        parent_vid_list = metadata.load_parent_id(table_name)
        click.echo("Parent dataset is %s " % parent_vid_list[0])
        click.echo("Parent versions are %s " % parent_vid_list[1])
    except Exception as e:
        click.secho(str(e), fg='red')
        return
    parent_name = parent_vid_list[0]
    parent_list = parent_vid_list[1]
    datatable_name = parent_name + "_datatable"
    indextable_name = parent_name + "_indexTbl"
    graph_name = parent_name + "_version"

    # exclduing rid
    

    # convert file into tmp_table first, then set the table_name to tmp_table
    if file_name:
        if not schema:
            raise NotImplementedError("Need a schema source for file %s" %file_name)
            return
        file_path = ctx.obj['orpheus_home'] + inputfile
        relation.create_relation_force('tmp_table', schema)
        _attributes, _attributes_type = self.get_datatable_attribute(schema)
        relation.convert_csv_to_table(file_path, 'tmp_table', _attributes , delimeters=delimeters, header=header)
        table_name = 'tmp_table'


    if table_name:
        # find the new records
        try:
            _attributes, _attributes_type = self.get_datatable_attribute(datatable_name)
            commit_attributes, _ = self.get_datatable_attribute(table_name)
            if not set(_attributes) - set(commit_attributes):
                raise BadStateError("%s and %s have different attributes" % (table_name, datatable_name))
            lis_of_newrecords = relation.select_complement_table(table_name, datatable_name, attributes=_attributes)
            if not lis_of_newrecords:
                click.echo("Nothing to commit")
                return
            lis_of_newrecords = [map(str, list(x)) for x in lis_of_newrecords]
            lis_of_newrecords = map(lambda x : '(' + ','.join(x) + ')', lis_of_newrecords)
            # insert them into datatable
            new_rids = relation.update_datatable(datatable_name, lis_of_newrecords)

            # find the existing rids
            existing_rids = [t[0] for t in relation.select_intersection_table(table_name, datatable_name)]
            
            print new_rids, existing_rids
            current_version_rid = existing_rids + new_rids

            num_of_records = relation.get_number_of_rows(table_name)
            table_create_time = metadata.load_table_create_time(table_name)

            # update version graph
            curt_vid = version.update_version_graph(graph_name, num_of_records, parent_list, table_create_time, msg)

            # update index table
            version.update_index_table(indextable_name, curt_vid, current_version_rid)
        except Exception as e:
            click.secho(str(e), fg='red')
            return

    if file_name:
        # need to drop tmp_table? But dt matter
        pass
    # TODO: Before return, we may also need to clean table if any.

    click.echo("commited")



@cli.command()
@click.pass_context
def clean(ctx):
    config = ctx.obj
    open(config['meta_info'], 'w').close()
    f = open(config['meta_info'], 'w')
    f.write('{"file_map": {}, "table_map": {}, "table_created_time": {}, "merged_tables": []}')
    f.close()
    click.echo("meta_info cleaned")
    open(config['meta_modifiedIds'], 'w').close()
    f = open(config['meta_modifiedIds'], 'w')
    f.write('{}')
    f.close()
    click.echo("modifiedID cleaned")
