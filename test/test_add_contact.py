# -*- coding: utf-8 -*-
from model.contacts import Contacts
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testcontactdata = [Contacts(name="", lastname="", companyaddress="", email="", homenumber="")] + [
    Contacts(name="Иван", lastname="Иванов", companyaddress="Прелестная, 1")] + [
    Contacts(name=random_string("name", 5), lastname=random_string("lastname", 8), companyaddress=random_string("companyaddress", 6), email=random_string("email", 6), homenumber=random_string("homenumber", 7))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testcontactdata, ids=[repr(x) for x in testcontactdata])
def test_add_contact(app, contact):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.add_new_user(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


