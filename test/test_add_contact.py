# -*- coding: utf-8 -*-
import pytest

from fixture.appliance import Application
from model.contacts import Contacts


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_user(Contacts(name="Иван", middlename="Иванович", lastname="Иванов", nickname="Ван", company="Галактика", companyaddress="Планетная улица, 1", homenumber="111-11-11",
                          mobilenumber="+7 (111) 111-11-11", worknumber="999-99-99", faxnumber="888-88-88", email="ivan@ivan.ru",
                          homeaddress="Галактическая улица, 2", secondhomenumber="555-55-55", notes="No"))
    app.logout()

def test_add_another_contact(app):
    app.login(username="admin", password="secret")
    app.add_new_user(Contacts(name="Федор", middlename="Федорович", lastname="Федоров", nickname="Фед", company="Вселенная", companyaddress="Красивая улица, 1", homenumber="222-22-22",
                          mobilenumber="+7 (222) 222-22-22", worknumber="222-22-22", faxnumber="222-22-22", email="fedor@fedor.ru",
                          homeaddress="Галактическая улица, 4", secondhomenumber="555-55-55", notes="No"))
    app.logout()

