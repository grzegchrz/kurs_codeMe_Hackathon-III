from ldap3 import Server, Connection, SUBTREE, LEVEL, ALL
from at_ad import *
import random, requests
import string
from config import conn_ldap


def generate_pasword(letters_count, digits_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string


class User:

    def __init__(self, name, surname):
        self.domain_ad = "telemetria.lcl"
        self.domain_dns = "telemetria.eu"
        self.name = name
        self.surname = surname
        self.username = self.name + "." + self.surname
        self.user_password = generate_pasword(6, 2)
        self.email = self.name + "." + self.surname + "@" + self.domain_dns
        self.userDomainAccount = self.name + "." + self.surname + "@" + self.domain_ad
        self.userOU = f'CN={self.name + "." + self.surname},OU=Hackaton,DC=telemetria,DC=lcl'

    def create(self):
        userdn = f'CN={self.username},OU=Hackaton,DC=telemetria,DC=lcl'
        print("Add user Hackaton.User to container Hackaton\n")
        conn_ldap.add(userdn, attributes={
            'objectClass': ['organizationalPerson', 'person', 'top', 'user'],
            'sAMAccountName': self.name + "." + self.surname,
            'userPrincipalName': "{}@{}".format(self.username, self.domain_ad),
            'userPassword': self.user_password,
            'displayName': self.name + " " + self.surname,
            'mail': self.email
        })
        # conn_ldap.modify(userdn, {'userAccountControl': [('MODIFY_REPLACE', 512)]})


'''
    def create_email(self):
        API_URL = "https://mail.telemetria.eu/api/v1/add/mailbox -d -H "X-API-Key: 28837f83-2a6c-4973-acc1-8e5457596eea""
        api_Key = "28837f83-2a6c-4973-acc1-8e5457596eea"
        data = f'{"local_part":"test","domain":"{self.domain_dns}","name":"{self.username}","quota":"100","password":"{self.user_password}","password2":"moohoo","active":"1"}'
        response = requests.post(API_URL, data)
        
'''
user_ad = User('Jan', 'Kowalski')
user_ad.create()

print(user_ad.email)
print(user_ad.username)
print(user_ad.user_password)
