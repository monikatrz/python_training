# -*- coding: utf-8 -*-
from model.addres import Addres

def test_add_new_address(app):
    old_addres = app.addres.get_addres_list()
    addres = Addres(firstname="new", middlename="mmmm", lastname="bbbbb", nickname="abacdccc", title="tttttttt", company="cccccccccccc", address="adrrr", home="123456789", mobile="111222333", work="wwwwwww", fax="ffffff", email='mail@wp.pl', email2="mail2@wp.pl", email3="mail3@wp.pl", homepage="hhhh", address2="23233", phone2="1234567890", notes="notttttttt")
    app.addres.create(addres)
    assert len(old_addres) + 1 == app.addres.count()
    new_addres = app.addres.get_addres_list()
    old_addres.append(addres)
    assert sorted(old_addres, key=Addres.id_or_max) == sorted(new_addres, key=Addres.id_or_max)

