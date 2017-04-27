# -*- coding: utf-8 -*-

from model.gredit import GrEdit

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(GrEdit(edname="new edit name", edheader="new edit header", edfooter="new edit footer"))
    app.session.logout()