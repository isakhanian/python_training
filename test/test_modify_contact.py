# -*- coding: utf-8 -*-

from model.contacts import Contacts

def test_modify_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add_new_user(Contacts(name="Иван", middlename="Иванович", lastname="Иванов", nickname="Ван", company="Галактика", companyaddress="Планетная улица, 1", homenumber="111-11-11",
                          mobilenumber="+7 (111) 111-11-11", worknumber="999-99-99", faxnumber="888-88-88", email="ivan@ivan.ru",
                          homeaddress="Галактическая улица, 2", secondhomenumber="555-55-55", notes="No"))
    app.contacts.modify_first_contact(Contacts(homeaddress="Прелестная, 1", homenumber="1234567", mobilenumber="+71234567890", worknumber="9876543", faxnumber="8765432", email="fed@fed.ru"))