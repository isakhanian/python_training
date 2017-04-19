# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group_for_contacts import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        return wd

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def add_new_user(self, wd, group):
        # add new user
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(group.companyaddress)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(group.homenumber)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(group.mobilenumber)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(group.worknumber)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(group.faxnumber)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(group.email)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(group.homeaddress)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(group.secondhomenumber)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(group.notes)
        # enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def check_list(self, wd):
        # check list
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
    
    def test_add_contact(self):
        wd = self.open_home_page()
        self.login(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.add_new_user(wd, Group(name="Иван", middlename="Иванович", lastname="Иванов", nickname="Ван", company="Галактика", companyaddress="Планетная улица, 1", homenumber="111-11-11",
                          mobilenumber="+7 (111) 111-11-11", worknumber="999-99-99", faxnumber="888-88-88", email="ivan@ivan.ru",
                          homeaddress="Галактическая улица, 2", secondhomenumber="555-55-55", notes="No"))
        self.check_list(wd)
        self.logout(wd)

    def test_add_another_contact(self):
        wd = self.open_home_page()
        self.login(wd, username="admin", password="secret")
        self.open_contact_page(wd)
        self.add_new_user(wd, Group(name="Федор", middlename="Федорович", lastname="Федоров", nickname="Фед", company="Вселенная", companyaddress="Красивая улица, 1", homenumber="222-22-22",
                          mobilenumber="+7 (222) 222-22-22", worknumber="222-22-22", faxnumber="222-22-22", email="fedor@fedor.ru",
                          homeaddress="Галактическая улица, 4", secondhomenumber="555-55-55", notes="No"))
        self.check_list(wd)
        self.logout(wd)


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
