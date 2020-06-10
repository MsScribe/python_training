# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import ContactMainInfo

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
        self.logout(wd)

    def create_contact(self, wd, contactmaininfo):
        # open create new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact main information
        wd.find_element_by_name("firstname").send_keys(contactmaininfo.firstname)
        wd.find_element_by_name("middlename").send_keys(contactmaininfo.middlename)
        wd.find_element_by_name("lastname").send_keys(contactmaininfo.lastname)
        wd.find_element_by_name("nickname").send_keys(contactmaininfo.nickname)
        wd.find_element_by_name("title").send_keys(contactmaininfo.title)
        wd.find_element_by_name("company").send_keys(contactmaininfo.company)
        wd.find_element_by_name("address").send_keys(contactmaininfo.homeaddress)
        # fill contact phone information
        wd.find_element_by_name("home").send_keys(contactmaininfo.homephone)
        wd.find_element_by_name("mobile").send_keys(contactmaininfo.mobilephone)
        wd.find_element_by_name("work").send_keys(contactmaininfo.workphone)
        wd.find_element_by_name("fax").send_keys(contactmaininfo.faxphone)
        # fill contact email information
        wd.find_element_by_name("email").send_keys(contactmaininfo.email)
        wd.find_element_by_name("email2").send_keys(contactmaininfo.email2)
        wd.find_element_by_name("email3").send_keys(contactmaininfo.email3)
        # fill contact homepage
        wd.find_element_by_name("homepage").send_keys(contactmaininfo.homepage)
        # fill contact bday information
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contactmaininfo.bday)
        wd.find_element_by_xpath("//option[@value='" + contactmaininfo.bday + "']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contactmaininfo.bmonth)
        wd.find_element_by_xpath("//option[@value='" + contactmaininfo.bmonth + "']").click()
        wd.find_element_by_name("byear").send_keys(contactmaininfo.byear)
        # fill contact anniversary
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contactmaininfo.aday)
        wd.find_element_by_xpath("(//option[@value='" + contactmaininfo.aday + "'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contactmaininfo.amonth)
        wd.find_element_by_xpath("(//option[@value='" + contactmaininfo.amonth + "'])[2]").click()
        wd.find_element_by_name("ayear").send_keys(contactmaininfo.ayear)
        # fill contact secondary information
        wd.find_element_by_name("address2").send_keys(contactmaininfo.address2)
        wd.find_element_by_name("phone2").send_keys(contactmaininfo.phone2)
        wd.find_element_by_name("notes").send_keys(contactmaininfo.notes)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
