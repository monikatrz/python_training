# -*- coding: utf-8 -*-
from model.addres import Addres
import pytest
import random
import string

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

@pytest.mark.parametrize("addres", testdata, ids=[repr(x) for x in testdata])
def test_add_new_addres(app, addres):
        old_addres = app.addres.get_addres_list()
        app.addres.create(addres)
        assert len(old_addres) + 1 == app.addres.count()
        new_addres = app.addres.get_addres_list()
        old_addres.append(addres)
        assert sorted(old_addres, key=Addres.id_or_max) == sorted(new_addres, key=Addres.id_or_max)