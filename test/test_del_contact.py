# -*- coding: utf-8 -*-

def test_delete_first_contact(app):
    app.contacts.delete_first_contact()