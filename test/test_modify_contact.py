# -*- coding: utf-8 -*-

from model.contacts import Contacts
from random import randrange

def test_modify_first_contact_more(app):
    if app.contacts.count() == 0:
        app.contacts.add_new_user(Contacts(name="Иван", middlename="Иванович", lastname="Иванов", nickname="Ван", company="Галактика", companyaddress="Планетная улица, 1", homenumber="111-11-11",
                          mobilenumber="+7 (111) 111-11-11", worknumber="999-99-99", faxnumber="888-88-88", email="ivan@ivan.ru",
                          homeaddress="Галактическая улица, 2", secondhomenumber="555-55-55", notes="No"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contacts(name="Семен", lastname="Семенов", homeaddress="Прелестная, 1", homenumber="1234567", mobilenumber="+71234567890", worknumber="9876543", faxnumber="8765432", email="fed@fed.ru")
    contact.id = old_contacts[index].id
    app.contacts.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[index] = contact
    print(old_contacts)
    print(new_contacts)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)


#def test_modify_first_contact_less(app):
    #if app.contacts.count() == 0:
        #app.contacts.add_new_user(Contacts(name="Иван", middlename="Иванович", lastname="Иванов", nickname="Ван", company="Галактика", companyaddress="Планетная улица, 1", homenumber="111-11-11",
                          #mobilenumber="+7 (111) 111-11-11", worknumber="999-99-99", faxnumber="888-88-88", email="ivan@ivan.ru",
                          #homeaddress="Галактическая улица, 2", secondhomenumber="555-55-55", notes="No"))
    #old_contacts = app.contacts.get_contact_list()
    #index = randrange(len(old_contacts))
    #contact = Contacts(name="Василий", lastname="Васильевич", email="fed@fed.ru")
    #contact.id = old_contacts[index].id
    #app.contacts.modify_contact_by_index(index, contact)
    #assert len(old_contacts) == app.contacts.count()
    #new_contacts = app.contacts.get_contact_list()
    #old_contacts[index] = contact
    #assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)