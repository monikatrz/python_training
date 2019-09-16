


def test_delete_first_address2(app):
    app.session.login(username="admin", password="secret")
    app.addres.delete_first_address2()
    app.session.logout()