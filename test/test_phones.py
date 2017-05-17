import re

def test_phones_on_home_page(app):
    contacts_from_home_page = app.contacts.get_contact_list()[0]
    contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contacts_from_home_page.homenumber == clear(contacts_from_edit_page.homenumber)
    assert contacts_from_home_page.mobilenumber == clear(contacts_from_edit_page.mobilenumber)
    assert contacts_from_home_page.worknumber == clear(contacts_from_edit_page.worknumber)
    assert contacts_from_home_page.secondhomenumber == clear(contacts_from_edit_page.secondhomenumber)

def test_phones_on_contact__view_page(app):
    contacts_from_view_page = app.contacts.get_contact_from_view_page(0)
    contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contacts_from_view_page.homenumber == (contacts_from_edit_page.homenumber)
    assert contacts_from_view_page.mobilenumber == (contacts_from_edit_page.mobilenumber)
    assert contacts_from_view_page.worknumber == (contacts_from_edit_page.worknumber)
    assert contacts_from_view_page.secondhomenumber == (contacts_from_edit_page.secondhomenumber)

def clear(s):
    return re.sub("[() -]", "", s)