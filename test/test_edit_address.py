# -*- coding: utf-8 -*-
from model.addres import Addres
from random import randrange

def test_edit_some_addres(app):
    if app.addres.count() == 0:
        app.addres.create(addres)
    old_addres = app.addres.get_addres_list()
    index = randrange(len(old_addres))
    addres = Addres(firstname="nnnnnnnnnnnnn", middlename="cccccccccc", lastname="tttgggttttt")
    addres.id = old_addres[index].id
    app.addres.edit_addres_by_index(index, addres)
    assert len(old_addres) == app.addres.count()
    new_addres = app.addres.get_addres_list()
    old_addres[index] = addres
    assert sorted(old_addres, key=Addres.id_or_max) == sorted(new_addres, key=Addres.id_or_max)