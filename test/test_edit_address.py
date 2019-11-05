# -*- coding: utf-8 -*-
from model.addres import Addres
import random

def test_edit_some_addres(app, db, check_ui):
    if len(db.get_addres_list()) == 0:
        app.addres.create(Addres(firstname="jestem"))
    old_addres = db.get_addres_list()
    addres = random.choice(old_addres)
    edit_addres = Addres(firstname="nnnnnnnnnnnnn", middlename="cccccccccc", lastname="tttgggttttt")
    app.addres.edit_addres_by_id(addres.id, edit_addres)
    new_addres = db.get_addres_list()
    assert len(old_addres) == len(new_addres)
    if check_ui:
        assert sorted(old_addres, key=Addres.id_or_max) == sorted(new_addres, key=Addres.id_or_max)