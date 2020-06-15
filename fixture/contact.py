from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contactmaininfo):
        wd = self.app.wd
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