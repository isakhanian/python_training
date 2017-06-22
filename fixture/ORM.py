from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contacts import Contacts
from pymysql.converters import decoders

class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        name = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        companyaddress = Optional(str, column='address')
        email = Optional(str, column='email')
        homenumber = Optional(str, column='home')
        deprecated = Optional(str, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_models(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_models(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_models(self, contacts):
        def convert(contact):
            return Contacts(id=str(contact.id), name=contact.name, lastname=contact.lastname, companyaddress=contact.companyaddress, email=contact.email, homenumber=contact.homenumber)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_models(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_models(orm_group.contacts)