# -*- coding: utf-8 -*-
from model.contacts import Contacts
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testcontactdata = [Contacts(name="", lastname="", companyaddress="", email="", homenumber="")] + [
    Contacts(name="Иван", lastname="Иванов", companyaddress="Прелестная, 1")] + [
    Contacts(name=random_string("name", 5), lastname=random_string("lastname", 8), companyaddress=random_string("companyaddress", 6), email=random_string("email", 6), homenumber=random_string("homenumber", 7))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testcontactdata, default=lambda x: x.__dict__, indent=2))