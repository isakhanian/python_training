# -*- coding: utf-8 -*-

from model.contedit import ContEdit

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contacts.edit_first_contact(ContEdit(edaddress="Прелестная, 1", edhomenumber="1234567", edmobilenumber="+71234567890", edworknumber="9876543", edfaxnumber="8765432", edemail="fed@fed.ru"))
    app.session.logout()