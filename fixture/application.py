from selenium import webdriver
from selenium.webdriver.support.select import Select
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    # def logout(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("Logout").click()

    # def return_to_groups(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("groups").click()
    #
    # def create_group(self, group):
    #     wd = self.wd
    #     self.open_groups_page()
    #     # init group creation
    #     wd.find_element_by_name("new").click()
    #     # fill group firm
    #     wd.find_element_by_name("group_name").send_keys(group.name)
    #     wd.find_element_by_name("group_header").send_keys(group.header)
    #     wd.find_element_by_name("group_footer").send_keys(group.footer)
    #     # submit group creation
    #     wd.find_element_by_name("submit").click()
    #     self.return_to_groups()
    #
    # def open_groups_page(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("groups").click()

    # def login(self, username, password):
    #     wd = self.wd
    #     self.open_home_page()
    #     wd.find_element_by_name("user").send_keys(username)
    #     wd.find_element_by_name("pass").send_keys(password)
    #     wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def create_contact(self, contactmaininfo):
        wd = self.wd
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