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
        self.change_field("name", contacts.name)
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

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.check_list()
        # select first contact
        # modify first contact
        self.select_first_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.check_list()


    def delete_first_contact(self):
        wd = self.app.wd
        self.check_list()
        # select first contact
        # delete first contact
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.check_list()

    def count(self):
        wd = self.app.wd
        self.check_list()
        return len(wd.find_elements_by_name("selected[]"))





