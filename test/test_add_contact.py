# -*- coding: utf-8 -*-
from model.contacts import Contacts
#from data.contacts import testcontactdata
#from data.contacts import constant as testcontactdata
#import pytest


#@pytest.mark.parametrize("contact", testcontactdata, ids=[repr(x) for x in testcontactdata])

def test_add_contact(app, data_contacts):
    contact = data_contacts
    old_contacts = app.contacts.get_contact_list()
    app.contacts.add_new_user(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


