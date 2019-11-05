# -*- coding: utf-8 -*-
from model.group import Group
import random
import string

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    chars = "".join([random.choice(symbols) for i in range(random.randrange(5,maxlen))]).strip()
    return chars

def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name=random_string(20), header=random_string(30), footer=random_string(30)))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.edit_group_by_id(group.id, Group(name=random_string(20), header=random_string(30), footer=random_string(30)))
    #app.group.edit_group_by_id(group.id, Group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert len(old_groups) == len(new_groups)
        #assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#def test_edit_group_header(app):
 #   if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(header="new header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

