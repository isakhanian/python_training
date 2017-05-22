import re

def test_phones_on_home_page(app):
    contacts_from_home_page = app.contacts.get_contact_list()[0]
    contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contacts_from_home_page.all_numbers_from_home_page == merge_numbers_like_on_home_page(contacts_from_edit_page)
    assert contacts_from_home_page.all_mails_from_home_page == merge_mails_like_on_home_page(contacts_from_edit_page)
    assert contacts_from_home_page.name == contacts_from_edit_page.name
    assert contacts_from_home_page.lastname == contacts_from_edit_page.lastname
    assert contacts_from_home_page.companyaddress == contacts_from_edit_page.companyaddress

def clear(s):
    return re.sub("[() -]", "", s)

def merge_numbers_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contacts.homenumber, contacts.mobilenumber, contacts.worknumber, contacts.secondhomenumber]))))

def merge_mails_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contacts.email, contacts.email2, contacts.email3]))))