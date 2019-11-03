# -*- coding: utf-8 -*-
from model.addres import Addres
import random

def test_delete_some_address2(app, db, check_ui):
    if len(db.get_addres_list()) == 0:
       app.addres.create(Addres(firstname="nnnnnnnnnnnnn", middlename="cccccccccc", lastname="tttgggttttt"))
    old_addres = db.get_addres_list()
    addres = random.choice(old_addres)
    app.addres.delete_addres_by_id(addres.id)
    new_addres = db.get_addres_list()
    assert len(old_addres) - 1 == len(new_addres)
    old_addres.remove(addres)
    if check_ui:
        assert sorted(new_addres, key=Addres.id_or_max)== sorted(app.addres.get_addres_list())
