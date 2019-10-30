# -*- coding: utf-8 -*-
from model.addres import Addres

# @pytest.mark.parametrize("addres", testdata, ids=[repr(x) for x in testdata])
def test_add_new_addres(app, json_address):
        addres = json_address
        old_addres = app.addres.get_addres_list()
        app.addres.create(addres)
        assert len(old_addres) + 1 == app.addres.count()
        new_addres = app.addres.get_addres_list()
        old_addres.append(addres)
        assert sorted(old_addres, key=Addres.id_or_max) == sorted(new_addres, key=Addres.id_or_max)