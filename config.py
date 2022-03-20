from ldap3 import Server, Connection, SUBTREE, LEVEL, ALL
from ldap3.core.exceptions import LDAPException, LDAPBindError

server = Server("ldap://dc01.telemetria.lcl", port=389, use_ssl=False, get_info='ALL')

conn_ldap = Connection(server, user="py", password="r&dEt9pg$un4",
                       fast_decoder=True, auto_bind=True, auto_referrals=True, check_names=False, read_only=True,
                       lazy=False, raise_exceptions=False)

if not conn_ldap.bind():
    exit(conn_ldap.result)

