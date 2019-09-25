# -*- coding: utf-8 -*-
from model.addres import Addres

def test_edit_first_address(app):
    if app.addres.count() == 0:
        app.addres.create(Addres(firstname="aaaa", middlename="mmmm", lastname="bbbbb", nickname="abacdccc", title="tttttttt", company="cccccccccccc", address="adrrr", home="123456789", mobile="111222333", work="wwwwwww", fax="ffffff", mail='mail@wp.pl', mail2="mail2@wp.pl", mail3="mail3@wp.pl", homepage="hhhh", address2="23233", phone2="1234567890", notes="notttttttt"))
    app.addres.edit_first_address(Addres(firstname="new f", middlename="new m", lastname="new l", nickname="new n", title="new t", company="new c", address="new a", home="7", mobile="9", work="ww", fax="1", mail='m@wp.pl', mail2="w@wp.pl", mail3="3@wp.pl", homepage="h", address2="2", phone2="1", notes="new no"))
