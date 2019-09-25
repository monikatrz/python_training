__author__ = 'monika'
from model.addres import Addres

class AddresHelper:

    def __init__(self, app):
        self.app = app

    def create(self, addres):
        wd = self.app.wd
        # init address creation
        wd.find_element_by_link_text("add new").click()
        self.fill_form(addres)
        # submit address creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_address(self):
        wd = self.app.wd
        # select first address
        self.open_home()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()

    def edit_first_address(self, addres):
        wd = self.app.wd
        # select edit
        self.open_home()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_form(addres)
        # submit address edit
        wd.find_element_by_name("update").click()

    def fill_form(self, addres):
        wd = self.app.wd
        self.change_field_value("firstname", addres.firstname)
        self.change_field_value("middlename", addres.middlename)
        self.change_field_value("lastname", addres.lastname)
        self.change_field_value("nickname", addres.nickname)
        self.change_field_value("title", addres.title)
        self.change_field_value("company", addres.company)
        self.change_field_value("address", addres.address)
        self.change_field_value("home", addres.home)
        self.change_field_value("mobile", addres.mobile)
        self.change_field_value("work", addres.work)
        self.change_field_value("fax", addres.fax)
        self.change_field_value("email", addres.mail)
        self.change_field_value("email2", addres.mail2)
        self.change_field_value("email3", addres.mail3)
        self.change_field_value("homepage", addres.homepage)
        self.change_field_value("address2", addres.address2)
        self.change_field_value("phone2", addres.phone2)
        self.change_field_value("notes", addres.notes)

        # wd.find_element_by_name("firstname").click()
        # wd.find_element_by_name("firstname").clear()
        # wd.find_element_by_name("firstname").send_keys(addres.firstname)
        # wd.find_element_by_name("middlename").click()
        # wd.find_element_by_name("middlename").clear()
        # wd.find_element_by_name("middlename").send_keys(addres.middlename)
        # wd.find_element_by_name("lastname").click()
        # wd.find_element_by_name("lastname").clear()
        # wd.find_element_by_name("lastname").send_keys(addres.lastname)
        # wd.find_element_by_name("nickname").click()
        # wd.find_element_by_name("nickname").clear()
        # wd.find_element_by_name("nickname").send_keys(addres.nickname)
        # wd.find_element_by_name("title").click()
        # wd.find_element_by_name("title").clear()
        # wd.find_element_by_name("title").send_keys(addres.title)
        # wd.find_element_by_name("company").click()
        # wd.find_element_by_name("company").clear()
        # wd.find_element_by_name("company").send_keys(addres.company)
        # wd.find_element_by_name("address").click()
        # wd.find_element_by_name("address").clear()
        # wd.find_element_by_name("address").send_keys(addres.address)
        # wd.find_element_by_name("home").click()
        # wd.find_element_by_name("home").clear()
        # wd.find_element_by_name("home").send_keys(addres.home)
        # wd.find_element_by_name("mobile").click()
        # wd.find_element_by_name("mobile").clear()
        # wd.find_element_by_name("mobile").send_keys(addres.mobile)
        # wd.find_element_by_name("work").click()
        # wd.find_element_by_name("work").clear()
        # wd.find_element_by_name("work").send_keys(addres.work)
        # wd.find_element_by_name("fax").click()
        # wd.find_element_by_name("fax").clear()
        # wd.find_element_by_name("fax").send_keys(addres.fax)
        # wd.find_element_by_name("email").click()
        # wd.find_element_by_name("email").clear()
        # wd.find_element_by_name("email").send_keys(addres.mail)
        # wd.find_element_by_name("email2").click()
        # wd.find_element_by_name("email2").clear()
        # wd.find_element_by_name("email2").send_keys(addres.mail2)
        # wd.find_element_by_name("email3").click()
        # wd.find_element_by_name("email3").clear()
        # wd.find_element_by_name("email3").send_keys(addres.mail3)
        # wd.find_element_by_name("homepage").click()
        # wd.find_element_by_name("homepage").clear()
        # wd.find_element_by_name("homepage").send_keys(addres.homepage)
        # wd.find_element_by_name("address2").click()
        # wd.find_element_by_name("address2").clear()
        # wd.find_element_by_name("address2").send_keys(addres.address2)
        # wd.find_element_by_name("phone2").click()
        # wd.find_element_by_name("phone2").clear()
        # wd.find_element_by_name("phone2").send_keys(addres.phone2)
        # wd.find_element_by_name("notes").click()
        # wd.find_element_by_name("notes").clear()
        # wd.find_element_by_name("notes").send_keys(addres.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_all_address(self):
        wd = self.app.wd
        # select first address
        self.open_home()
        wd.find_element_by_id("MassCB").click()
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def delete_first_address2(self):
        wd = self.app.wd
        # select first address
        self.open_home()
        wd.find_element_by_name("selected[]").click()
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def open_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/.php")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements_by_name("selected[]"))