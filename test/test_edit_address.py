# -*- coding: utf-8 -*-
from model.addres import Addres

def test_edit_first_address(app):
    addres = Addres(firstname="nnnnnnnnnnnnn", middlename="cccccccccc", lastname="tttgggttttt")
    if app.addres.count() == 0:
        app.addres.create(addres)
    old_addres = app.addres.get_addres_list()
    addres.id = old_addres[0].id
    app.addres.edit_first_address(addres)
    assert len(old_addres) == app.addres.count()
    new_addres = app.addres.get_addres_list()
    old_addres[0] = addres
    assert sorted(old_addres, key=Addres.id_or_max) == sorted(new_addres, key=Addres.id_or_max)