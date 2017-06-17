# -*- coding: utf-8 -*-

from model.group import Group
import random

def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    mod_group = random.choice(old_groups) #задаем переменную, список, из которого будет выбирать элемент
    group = Group(name="new group")
    app.group.modify_group_by_id(mod_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    mod_group = random.choice(old_groups) #задаем переменную, список, из которого будет выбирать элемент
    group = Group(header="new header")
    app.group.modify_group_by_id(mod_group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_name(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="test"))
    #old_groups = app.group.get_group_list()
    #index = randrange(len(old_groups))
    #group = Group(name="new group")
    #group.id = old_groups[index].id
    #app.group.modify_group_by_index(index, group)
    #assert len(old_groups) == app.group.count()
    #new_groups = app.group.get_group_list()
    #old_groups[index] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="test"))
    #old_groups = app.group.get_group_list()
    #index = randrange(len(old_groups))
    #group = Group(name="newest_group", header="new header")
    #group.id = old_groups[index].id
    #app.group.modify_group_by_index(index, group)
    #assert len(old_groups) == app.group.count()
    #new_groups = app.group.get_group_list()
    #old_groups[index] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)