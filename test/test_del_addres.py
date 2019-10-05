# -*- coding: utf-8 -*-
from model.addres import Addres
from random import randrange


def test_delete_some_address2(app):
    addres = Addres(firstname="nnnnnnnnnnnnn", middlename="cccccccccc", lastname="tttgggttttt")
    if app.addres.count() == 0:
       app.addres.create(addres)
    old_addres = app.addres.get_addres_list()
    index = randrange(len(old_addres))
    app.addres.delete_addres_by_index(index)
    assert len(old_addres) - 1 == app.addres.count()
    new_addres = app.addres.get_addres_list()
    old_addres[index:index+1] = []
    assert old_addres == new_addres
