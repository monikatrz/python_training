# -*- coding: utf-8 -*-
import pytest
from model.addres import Addres
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_address(app):
    app.session.login(username="admin", password="secret")
    app.addres.create(Addres(firstname="aaaa", middlename="mmmm", lastname="bbbbb", nickname="abacdccc", title="tttttttt", company="cccccccccccc", address="adrrr", home="123456789", mobile="111222333", work="wwwwwww", fax="ffffff", mail='mail@wp.pl', mail2="mail2@wp.pl", mail3="mail3@wp.pl", homepage="hhhh", address2="23233", phone2="1234567890", notes="notttttttt"))
    app.session.logout()

