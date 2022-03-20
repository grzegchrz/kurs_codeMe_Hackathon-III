#!/usr/bin/python
# -*- coding: utf-8 -*-

import ldap3
import config
from ldap3 import Server, Connection, SUBTREE, LEVEL, ALL, ObjectDef, Reader
from ldap3.core.exceptions import LDAPException, LDAPBindError
from config import conn_ldap



def get_child_ou_dns(dn="OU=Hackaton,DC=telemetria,DC=lcl"):
    results = list()
    elements = conn_ldap.extend.standard.paged_search(
        search_base=dn,
        search_filter='(objectCategory=organizationalUnit)',
        search_scope=LEVEL,
        paged_size=100)
    for element in elements:
        if 'dn' in element:
            if element['dn'] != dn:
                if 'dn' in element:
                    results.append(element['dn'])
    print("Wyświetlenie kontenera Hackaton\n")
    return print(f'{results}\n')

'''
def view_all_members():
    user_group_dn = 'OU=Organization,OU=Groups,DC=telemetria,DC=lcl'
    search_filter = " (!(givenName=Smith))"
    search_attribute = ['memberOf', 'member', 'userPrincipalName']
    elements = conn_ldap.search(search_base=user_group_dn,
                            search_filter=search_filter,
                            attributes=search_attribute)
    for a in conn_ldap.entries:
        print(a)
'''
def view_member_in_group(group='DIT'):
    results = list()
    user_group_dn = 'OU=Hackaton,DC=telemetria,DC=lcl'
    search_filter = f"(cn={group})"
    search_attribute = ['mail', 'memberOf']
    elements = conn_ldap.search(search_base=user_group_dn,
                                search_scope=SUBTREE,
                                search_filter=search_filter,
                                attributes=search_attribute)

    print(elements)
    return print(memberOf[0])

def create_ldap_group(group="Hackaton.Group"):
    ldap_attr = {'objectClass': ['group']}
    print("Add group Hackaton.grupa do kontenera Hackaton\n")
    try:

        response = conn_ldap.add(f"CN={group},OU=Hackaton,DC=telemetria,DC=lcl",
                                 attributes=ldap_attr)
    except LDAPException as e:
        response = (" The error is ", e)
    return response


def create_ldap_user():
    domain = 'telemetria.lcl'
    username = 'Hackaton.User'
    useremail = 'Hackaton@user.com'
    userpswd = 'AbcDef$$1234567'
    userdn = f'CN={username},OU=Hackaton,DC=telemetria,DC=lcl'
    print("Add user Hackaton.User do kontenera Hackaton\n")
    conn_ldap.add(userdn, attributes={
        'objectClass': ['organizationalPerson', 'person', 'top', 'user'],
        'sAMAccountName': username,
        'userPrincipalName': "{}@{}".format(username, domain),
        'displayName': username,
        'mail': useremail
    })


