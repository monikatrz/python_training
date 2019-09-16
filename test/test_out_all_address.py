

def test_delete_all_address(app):
    app.session.login(username="admin", password="secret")
    app.addres.delete_all_address()
    app.session.logout()