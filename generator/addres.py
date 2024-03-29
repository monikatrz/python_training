from model.addres import Addres
import random
import string
import os.path
import jsonpickle
import getopt
import sys
import pytest

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ['number of groups', "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/address.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Addres(firstname="", middlename="", lastname="", nickname="", title="", company="",
            address="", home="", mobile="", work="", fax="", email="", email2="",
            email3="", homepage="", address2="", phone2="", notes="")] + [
    Addres(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 20), nickname=random_string("nickname", 10), title=random_string("title", 20), company=random_string("company", 10),
            address=random_string("address", 30), home=random_string("home", 10), mobile=random_string("mobile", 10), work=random_string("work", 10), fax=random_string("fax", 10), email=random_string("email", 20), email2=random_string("email2", 20),
            email3=random_string("email3", 20),  homepage=random_string("homepage", 20), address2=random_string("address2", 20), phone2=random_string("phone2", 10), notes=random_string("notes", 20))
    for i in range(5)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))