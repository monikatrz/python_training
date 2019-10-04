# -*- coding: utf-8 -*-
from model.addres import Addres


def test_delete_first_address2(app):
    addres = Addres(firstname="nnnnnnnnnnnnn", middlename="cccccccccc", lastname="tttgggttttt")
    if app.addres.count() == 0:
       app.addres.create(addres)
    old_addres = app.addres.get_addres_list()
    app.addres.delete_first_address2()
    assert len(old_addres) - 1 == app.addres.count()
    new_addres = app.addres.get_addres_list()
    old_addres[0:1] = []
    assert old_addres == new_addres
