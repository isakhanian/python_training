# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="new", header="newheader", footer="newfooter"))
    app.session.logout()

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
