# -*- coding: utf-8 -*-
import contact
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from contact import ContactMainInfo, ContactPhoneInfo, ContactEmail, ContactHomePage, ContactBDay, ContactADay, ContactSecInfo

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest",
                                                lastname="LastNameTest", nickname="NickNameTest", title="TestTitle",
                                                company="TestCompany", homeaddress="Test Street Test home"),
                            ContactPhoneInfo("9998887766", "+79876543210", "+567", "3456"),
                            ContactEmail("123qwert@test.ru",
                                         "1234qwsa@test.com", "test123@test.ru"), ContactHomePage("hhtps://test.ru"),
                            ContactBDay("1", "July", "1990"), ContactADay("6", "November", "1987"), ContactSecInfo("Street address",
                            "testhome", "blablabla"))
        self.logout(wd)

    def create_contact(self, wd, contactmaininfo, contactphone, contactemail, contacthomepage, contactbday, contactaday,
                       contactsecinfo):
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
        wd.find_element_by_name("home").send_keys(contactphone.homephone)
        wd.find_element_by_name("mobile").send_keys(contactphone.mobilephone)
        wd.find_element_by_name("work").send_keys(contactphone.workphone)
        wd.find_element_by_name("fax").send_keys(contactphone.faxphone)
        # fill contact email information
        wd.find_element_by_name("email").send_keys(contactemail.email)
        wd.find_element_by_name("email2").send_keys(contactemail.email2)
        wd.find_element_by_name("email3").send_keys(contactemail.email3)
        # fill contact homepage
        wd.find_element_by_name("homepage").send_keys(contacthomepage.homepage)
        # fill contact bday information
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contactbday.bday)
        wd.find_element_by_xpath("//option[@value='" + contactbday.bday + "']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contactbday.bmonth)
        wd.find_element_by_xpath("//option[@value='" + contactbday.bmonth + "']").click()
        wd.find_element_by_name("byear").send_keys(contactbday.byear)
        # fill contact anniversary
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contactaday.aday)
        wd.find_element_by_xpath("(//option[@value='" + contactaday.aday + "'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contactaday.amonth)
        wd.find_element_by_xpath("(//option[@value='" + contactaday.amonth + "'])[2]").click()
        wd.find_element_by_name("ayear").send_keys(contactaday.ayear)
        # fill contact secondary information
        wd.find_element_by_name("address2").send_keys(contactsecinfo.address2)
        wd.find_element_by_name("phone2").send_keys(contactsecinfo.phone2)
        wd.find_element_by_name("notes").send_keys(contactsecinfo.notes)
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
