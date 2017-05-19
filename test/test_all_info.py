import re

def test_phones_on_home_page(app):
    contacts_from_home_page = app.contacts.get_contact_list()[0]
    contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contacts_from_home_page.all_numbers_from_home_page == merge_numbers_like_on_home_page(contacts_from_edit_page)

def test_phones_on_contact_view_page(app):
    name_from_view_page = app.contacts.get_contact_from_view_page(0)
    name_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contacts_from_view_page.homenumber == (contacts_from_edit_page.homenumber)
    assert contacts_from_view_page.mobilenumber == (contacts_from_edit_page.mobilenumber)
    assert contacts_from_view_page.worknumber == (contacts_from_edit_page.worknumber)
    assert contacts_from_view_page.secondhomenumber == (contacts_from_edit_page.secondhomenumber)



def clear(s):
    return re.sub("[() -]", "", s)

def merge_numbers_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
