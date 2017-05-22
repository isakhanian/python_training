from sys import maxsize
class Contacts:

    def __init__(self, name = None, middlename = None, lastname = None, nickname = None, company = None, companyaddress = None, homenumber = None, mobilenumber = None,
                     worknumber = None, faxnumber = None, email = None, email2 = None, email3 = None, homeaddress = None, secondhomenumber = None, notes = None, id = None, all_numbers_from_home_page=None, all_mails_from_home_page = None):
        self.name = name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.companyaddress = companyaddress
        self.homenumber = homenumber
        self.mobilenumber = mobilenumber
        self.worknumber = worknumber
        self.faxnumber = faxnumber
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homeaddress = homeaddress
        self.secondhomenumber = secondhomenumber
        self.notes = notes
        self.id = id
        self.all_numbers_from_home_page = all_numbers_from_home_page
        self.all_mails_from_home_page = all_mails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize