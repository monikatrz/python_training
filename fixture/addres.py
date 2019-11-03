__author__ = 'monika'
from model.addres import Addres
import re

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
        self.addres_cache = None

#    def delete_first_address(self):
#        wd = self.app.wd
#        # select first address
#        self.open_home()
#        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # submit deletion
#        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()

    def edit_first_addres(self):
        self.edit_addres_by_index(0)

    def select_addres_edit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def edit_addres_by_index(self, index, addres):
        wd = self.app.wd
        # select edit
     #   self.open_home()
        self.select_addres_edit_by_index(index)
        self.fill_form(addres)
        # submit address edit
        wd.find_element_by_name("update").click()
        self.addres_cache = None

    def edit_addres_by_id(self, id, addres):
        wd = self.app.wd
        # select edit
     #   self.open_home()
        self.select_addres_edit_by_id(id)
        self.fill_form(addres)
        # submit address edit
        wd.find_element_by_name("update").click()
        self.addres_cache = None

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
        self.change_field_value("email", addres.email)
        self.change_field_value("email2", addres.email2)
        self.change_field_value("email3", addres.email3)
        self.change_field_value("homepage", addres.homepage)
        self.change_field_value("address2", addres.address2)
        self.change_field_value("phone2", addres.phone2)
        self.change_field_value("notes", addres.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

 #   def delete_all_address(self):
 #       wd = self.app.wd
 #       # select first address
 #       self.open_home()
 #       wd.find_element_by_id("MassCB").click()
 #       self.accept_next_alert = True
 #       wd.find_element_by_xpath("//input[@value='Delete']").click()
 #       wd.switch_to_alert().accept()

    def select_first_addres(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_addres_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_addres_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_address2(self):
        self.delete_addres_by_index(0)

    def delete_addres_by_index(self, index):
        wd = self.app.wd
        # select first address
        self.open_home()
        self.select_addres_by_index(index)
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.addres_cache = None

    def delete_addres_by_id(self, id):
        wd = self.app.wd
        # select first address
        self.open_home()
        self.select_addres_by_id(id)
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.addres_cache = None

    def open_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements_by_name("selected[]"))

    addres_cache = None

    def get_addres_list(self):
        if self.addres_cache is None:
            wd = self.app.wd
            self.open_home()
            self.addres_cache = []
            for element in wd.find_elements_by_name("entry"): #row
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                lastname_text = cells[1].text
                firstname_text = cells[2].text
                address_text = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.addres_cache.append(Addres(lastname=lastname_text, firstname=firstname_text, id=id, address=address_text, all_emails_from_homepage=all_emails, all_phones_from_homepage=all_phones))
            return list(self.addres_cache)

    def select_addres_edit_by_index(self, index):
        wd = self.app.wd
     #   wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.open_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def select_addres_edit_by_id(self, id):
        wd = self.app.wd
     #   wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.open_home()
        wd.find_element_by_xpath("//a[contains(@href, 'edit.php?id=%s')]" % id).click()

    def select_addres_view_by_index(self, index):
        wd = self.app.wd
     #   wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.open_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_addres_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_addres_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Addres(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2, email3=email3,  home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone)

    def get_addres_info_from_view_page(self, index):
        wd = self.app.wd
        self.select_addres_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Addres(firstname=firstname, lastname=lastname, id=id, home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone)

    def get_addres_from_view_page(self, index):
        wd = self.app.wd
        self.select_addres_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Addres(home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone)