# -*- coding: utf-8 -*-
from model.contacts import Contacts
import random
import string



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testcontactdata = [Contacts(name="", lastname="", companyaddress="", email="", homenumber="")] + [
    Contacts(name="Иван", lastname="Иванов", companyaddress="Прелестная, 1")] + [
    Contacts(name=random_string("name", 5), lastname=random_string("lastname", 8), companyaddress=random_string("companyaddress", 6), email=random_string("email", 6), homenumber=random_string("homenumber", 7))
    for i in range(5)
]


constant = [
    Contacts(name="name1", lastname="lastname1", email="email1"),
    Contacts(name="name2", lastname="lastname2", email="email2")
]