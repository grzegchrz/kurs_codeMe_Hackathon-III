#!/usr/bin/env python
import config, click
from ldap3 import Server, Connection, SUBTREE, LEVEL, ALL
from at_ad import *


@click.group("first-level")
def cli():
    """Top level"""


@cli.group("create")
def second_create():
    """create user, group """


@cli.group("view")
def second_view():
    """view group"""


@second_create.command()
def user():
    """user add"""
    create_ldap_user()


@second_create.command()
def group():
    """group add"""
    create_ldap_group()


@second_view.command()
def ou():
    """view list in ou Hackaton"""
    get_child_ou_dns()


if __name__ == '__main__':
    cli()
