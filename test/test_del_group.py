# -*- coding: utf-8 -*-

from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        print("no any groups")
        app.group.create(Group(name="test"))
        app.group.delete_first_group()
    else:
        print("groups are here, delete")
        app.group.delete_first_group()

