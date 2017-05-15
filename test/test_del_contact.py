# -*- coding: utf-8 -*-

from model.contacts import Contacts

def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add_new_user(Contacts(name="Иван", middlename="Иванович", lastname="Иванов", nickname="Ван", company="Галактика", companyaddress="Планетная улица, 1", homenumber="111-11-11",
                          mobilenumber="+7 (111) 111-11-11", worknumber="999-99-99", faxnumber="888-88-88", email="ivan@ivan.ru",
                          homeaddress="Галактическая улица, 2", secondhomenumber="555-55-55", notes="No"))
    old_contacts = app.contacts.get_contact_list()
    app.contacts.delete_first_contact()
    assert len(old_contacts) - 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts [0:1] = []
    assert old_contacts == new_contacts