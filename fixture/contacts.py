from model.contacts import Contacts
import re

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def check_list(self):
        wd = self.app.wd
        if wd.current_url.endswith("/index.php") and len(wd.find_elements_by_xpath("//input[@value='Delete']")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contacts):
        wd = self.app.wd
        self.change_field("firstname", contacts.name)
        self.change_field("middlename", contacts.middlename)
        self.change_field("lastname", contacts.lastname)
        self.change_field("nickname", contacts.nickname)
        self.change_field("company", contacts.company)
        self.change_field("address", contacts.companyaddress)
        self.change_field("home", contacts.homenumber)
        self.change_field("mobile", contacts.mobilenumber)
        self.change_field("work", contacts.worknumber)
        self.change_field("fax", contacts.faxnumber)
        self.change_field("email", contacts.email)
        self.change_field("address2", contacts.homeaddress)
        self.change_field("phone2", contacts.secondhomenumber)
        self.change_field("notes", contacts.notes)


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def add_new_user(self, contacts):
        wd = self.app.wd
        self.open_contact_page()
        # add new user
        self.fill_contact_form(contacts)
        # enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.check_list()
        self.contact_cash = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0, new_contact_data)


    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.check_list()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.check_list()
            self.contact_cash = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                lastname = cells[1].text
                name = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_numbers = cells[5].text.splitlines()
                self.contact_cash.append(Contacts(name=name, lastname=lastname, id=id,
                                                  homenumber=all_numbers[0], mobilenumber=all_numbers[1],
                                                  worknumber=all_numbers[2], secondhomenumber=all_numbers[3]))
        return list(self.contact_cash)


    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.check_list()
        self.select_contact_by_index(index)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.check_list()
        self.contact_cash = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.check_list()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.check_list()
        self.contact_cash = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.check_list()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.check_list()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homenumber = wd.find_element_by_name("home").get_attribute("value")
        mobilenumber = wd.find_element_by_name("mobile").get_attribute("value")
        worknumber = wd.find_element_by_name("work").get_attribute("value")
        secondhomenumber = wd.find_element_by_name("phone2").get_attribute("value")
        return Contacts(name=name, lastname=lastname, id=id, homenumber=homenumber,
                        mobilenumber=mobilenumber, worknumber=worknumber,
                        secondhomenumber=secondhomenumber)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homenumber = re.search("H: (.*)", text).group(1)
        mobilenumber = re.search("M: (.*)", text).group(1)
        worknumber = re.search("W: (.*)", text).group(1)
        secondhomenumber = re.search("P: (.*)", text).group(1)
        return Contacts(homenumber=homenumber,
                        mobilenumber=mobilenumber, worknumber=worknumber,
                        secondhomenumber=secondhomenumber)