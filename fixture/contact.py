from model.contact import ContactMainInfo
from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_link_text("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

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
        wd = self.app.wd
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

    def modify_first_contact(self, contactmaininfo):
        wd = self.app.wd
        self.open_contact_page()
        # open edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contactmaininfo)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.open_contact_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # open edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contact_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.group_cache = []
            count = len(wd.find_elements_by_xpath("//input[@name='selected[]']"))
            for i in range(2, count+2):
                lastname = wd.find_element_by_xpath("//tr[" + str(i) + "]//input[@name='selected[]']/../../td[2]").text
                firstname = wd.find_element_by_xpath("//tr[" + str(i) + "]//input[@name='selected[]']/../../td[3]").text
                id = wd.find_element_by_xpath("//tr[" + str(i) + "]//input[@name='selected[]']").get_attribute("value")
                self.group_cache.append(ContactMainInfo(id=id, firstname=firstname, lastname=lastname))
        return list(self.group_cache)