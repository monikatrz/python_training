# -*- coding: utf-8 -*-
from model.addres import Addres

def test_edit_first_address(app):
    app.session.login(username="admin", password="secret")
    app.addres.edit_first_address(Addres(firstname="f", middlename="m", lastname="l", nickname="n", title="t", company="c", address="a", home="7", mobile="9", work="ww", fax="1", mail='m@wp.pl', mail2="w@wp.pl", mail3="3@wp.pl", homepage="h", address2="2", phone2="1", notes="no"))
    app.session.logout()