# -*- coding: utf-8 -*-

from model.contacts import Contacts
from random import randrange
import random


def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contacts.add_new_user(Contacts(name="Иван", middlename="Иванович", lastname="Иванов", nickname="Ван", company="Галактика", companyaddress="Планетная улица, 1", homenumber="111-11-11",
                          mobilenumber="+7 (111) 111-11-11", worknumber="999-99-99", faxnumber="888-88-88", email="ivan@ivan.ru",
                          homeaddress="Галактическая улица, 2", secondhomenumber="555-55-55", notes="No"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contact_list(), key=Contacts.id_or_max)


#def test_delete_first_contact(app):
    #if app.contacts.count() == 0:
        #app.contacts.add_new_user(Contacts(name="Иван", middlename="Иванович", lastname="Иванов", nickname="Ван", company="Галактика", companyaddress="Планетная улица, 1", homenumber="111-11-11",
                          #mobilenumber="+7 (111) 111-11-11", worknumber="999-99-99", faxnumber="888-88-88", email="ivan@ivan.ru",
                          #homeaddress="Галактическая улица, 2", secondhomenumber="555-55-55", notes="No"))
    #old_contacts = app.contacts.get_contact_list()
    #index = randrange(len(old_contacts))
    #app.contacts.delete_contact_by_index(index)
    #assert len(old_contacts) - 1 == app.contacts.count()
    #new_contacts = app.contacts.get_contact_list()
    #old_contacts [index:index+1] = []
    #assert old_contacts == new_contacts