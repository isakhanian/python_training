# -*- coding: utf-8 -*-
from model.contacts import Contacts



def test_add_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(name="Иван", middlename="Иванович", lastname="Иванов", nickname="Ван", company="Галактика", companyaddress="Планетная улица, 1", homenumber="1111111",
                          mobilenumber="+71111111111", worknumber="9999999", faxnumber="8888888", email="ivan@ivan.ru",
                          homeaddress="Галактическая улица, 2", secondhomenumber="5555555", notes="No")
    app.contacts.add_new_user(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

def test_add_another_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(name="Федор", middlename="Федорович", lastname="Федоров", nickname="Фед", company="Вселенная", companyaddress="Красивая улица, 1", homenumber="2222222",
                          mobilenumber="+72222222222", worknumber="2222222", faxnumber="2222222", email="fedor@fedor.ru",
                          homeaddress="Галактическая улица, 4", secondhomenumber="5555555", notes="No")
    app.contacts.add_new_user(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

