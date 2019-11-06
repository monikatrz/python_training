import re
from model.addres import Addres

def test_all_address_on_homepage_with_db(app, db):
    list_range = len(db.get_addres_list())
    for row in range(list_range):
        addres_from_home_page = sorted(app.addres.get_addres_list(), key=Addres.id_or_max)[row]
        addres_from_db = sorted(db.get_addres_list(), key=Addres.id_or_max)[row]
        assert sorted(addres_from_db.lastname) == sorted(addres_from_home_page.lastname)
        assert sorted(addres_from_db.firstname) == sorted(addres_from_home_page.firstname)
        assert sorted(address_clean(addres_from_db.address)) == sorted(addres_from_home_page.address)
        assert sorted(merge_phones_like_on_home_page(addres_from_db)) == sorted(
            addres_from_home_page.all_phones_from_homepage)
        assert sorted(merge_emails_like_on_home_page(addres_from_db)) == sorted(
            addres_from_home_page.all_emails_from_homepage)

def test_phones_on_home_page(app):
    addres_from_home_page = app.addres.get_addres_list()[0]
    addres_from_edit_page = app.addres.get_addres_info_from_edit_page(0)
    assert sorted(addres_from_home_page.all_phones_from_homepage) == sorted(merge_phones_like_on_home_page(addres_from_edit_page))

def test_phones_on_view_page(app):
    addres_from_view_page = app.addres.get_addres_from_view_page(0)
    addres_from_edit_page = app.addres.get_addres_info_from_edit_page(0)
    assert addres_from_view_page.home == addres_from_edit_page.home
    assert addres_from_view_page.work == addres_from_edit_page.work
    assert addres_from_view_page.mobile == addres_from_edit_page.mobile
    assert addres_from_view_page.phone2 == addres_from_edit_page.phone2

def test_names_on_home_page(app):
    addres_from_home_page = app.addres.get_addres_list()[0]
    addres_from_edit_page = app.addres.get_addres_info_from_edit_page(0)
    assert addres_from_home_page.lastname == addres_from_edit_page.lastname
    assert addres_from_home_page.firstname == addres_from_edit_page.firstname

def test_address_on_home_page(app):
    addres_from_home_page = app.addres.get_addres_list()[0]
    addres_from_edit_page = app.addres.get_addres_info_from_edit_page(0)
    assert addres_from_home_page.address == addres_from_edit_page.address

def test_emails_on_home_page(app):
    addres_from_home_page = app.addres.get_addres_list()[0]
    addres_from_edit_page = app.addres.get_addres_info_from_edit_page(0)
    assert sorted(addres_from_home_page.all_emails_from_homepage) == sorted(merge_emails_like_on_home_page(addres_from_edit_page))

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(addres):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [addres.home, addres.work, addres.mobile, addres.phone2]))))

def merge_emails_like_on_home_page(addres):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [addres.email, addres.email2, addres.email3])))

def address_clean(s):
    return re.sub("  ", " ", s)