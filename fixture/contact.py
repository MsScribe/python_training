from model.contact import ContactMainInfo
from selenium.webdriver.support.select import Select
import re
import random


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_link_text("Send e-Mail")) > 0):
            wd.find_element_by_xpath("//a[text()='home']").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_day(self, field_date, date):
        wd = self.app.wd
        if date is not None:
            wd.find_element_by_name(field_date).click()
            Select(wd.find_element_by_name(field_date)).select_by_visible_text(date)
            wd.find_element_by_xpath("//option[@value='" + date + "']").click()

    def fill_contact_form(self, contactmaininfo):
        # fill contact main information
        self.change_field_value("firstname", contactmaininfo.firstname)
        self.change_field_value("middlename", contactmaininfo.middlename)
        self.change_field_value("lastname", contactmaininfo.lastname)
        self.change_field_value("nickname", contactmaininfo.nickname)
        self.change_field_value("title", contactmaininfo.title)
        self.change_field_value("company", contactmaininfo.company)
        self.change_field_value("address", contactmaininfo.homeaddress)
        # fill contact phone information
        self.change_field_value("home", contactmaininfo.homephone)
        self.change_field_value("mobile", contactmaininfo.mobilephone)
        self.change_field_value("work", contactmaininfo.workphone)
        self.change_field_value("fax", contactmaininfo.faxphone)
        # fill contact email information
        self.change_field_value("email", contactmaininfo.email)
        self.change_field_value("email2", contactmaininfo.email2)
        self.change_field_value("email3", contactmaininfo.email3)
        # fill contact homepage
        self.change_field_value("homepage", contactmaininfo.homepage)
        # fill contact bday information
        self.change_field_value_day("bday", contactmaininfo.bday)
        self.change_field_value_day("bmonth", contactmaininfo.bmonth)
        self.change_field_value("byear", contactmaininfo.byear)
        # fill contact anniversary
        self.change_field_value_day("aday", contactmaininfo.aday)
        self.change_field_value_day("amonth", contactmaininfo.amonth)
        self.change_field_value("ayear", contactmaininfo.ayear)
        # fill contact secondary information
        self.change_field_value("address2", contactmaininfo.address2)
        self.change_field_value("phone2", contactmaininfo.phone2)
        self.change_field_value("notes", contactmaininfo.notes)

    def select_group(self, group_name):
        wd = self.app.wd
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(group_name)

    def create(self, contactmaininfo):
        wd = self.app.wd
        self.open_contact_page()
        # open create new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contactmaininfo)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_contact_page()
        self.contact_cache = None

    def create_in_group(self, contactmaininfo, group_name):
        wd = self.app.wd
        self.open_contact_page()
        # open create new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contactmaininfo)
        self.select_group(group_name)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_contact_page()
        self.contact_cache = None

    def connect_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        # Выбрать контакт без группы
        wd.find_element_by_css_selector("input[value='%s']" % contact_id).click()
        # Выбрать группу без контакта
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)
        # Сохранить
        wd.find_element_by_name("add").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        # open edit contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        # open edit contact
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//td[7]/a")[index].click()

    def modify_contact_by_index(self, index, contactmaininfo):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contactmaininfo)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, contactmaininfo):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contactmaininfo)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # open edit contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contact_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            count = len(wd.find_elements_by_xpath("//input[@name='selected[]']"))
            for i in range(2, count+2):
                lastname = wd.find_element_by_xpath("//tr[" + str(i) + "]//input[@name='selected[]']/../../td[2]").text
                firstname = wd.find_element_by_xpath("//tr[" + str(i) + "]//input[@name='selected[]']/../../td[3]").text
                id = wd.find_element_by_xpath("//tr[" + str(i) + "]//input[@name='selected[]']").get_attribute("value")
                all_phones = wd.find_element_by_xpath("//tr[" + str(i) + "]//input[@name='selected[]']/../../td[6]").text
                all_emails = wd.find_element_by_xpath("//tr[" + str(i) + "]//input[@name='selected[]']/../../td[5]").text
                address = wd.find_element_by_xpath("//tr[" + str(i) + "]//input[@name='selected[]']/../../td[4]").text
                self.contact_cache.append(ContactMainInfo(id=id, firstname=firstname, lastname=lastname, all_phones_from_home_page=clear(all_phones), all_emails_from_home_page=clear(all_emails), homeaddress=address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_page()
        self.open_contact_to_edit_by_index(index)
        return self.get_contact_info()

    def get_contact_info(self):
        wd = self.app.wd
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return ContactMainInfo(id=id, firstname=firstname, lastname=lastname, homephone=homephone, mobilephone=mobilephone, workphone=workphone, phone2=phone2, email=email, email2=email2, email3=email3, homeaddress=address)


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return ContactMainInfo(homephone=homephone, mobilephone=mobilephone, workphone=workphone, phone2=phone2)

def clear(s):
    return re.sub("[() - \n]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.all_phones, contact.mobilephone, contact.workphone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))