class ContactMainInfo:
    def __init__(self, firstname, middlename, lastname, nickname, title, company, homeaddress):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.homeaddress = homeaddress

class ContactPhoneInfo:
    def __init__(self, homephone, mobilephone, workphone, faxphone):
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.faxphone = faxphone

class ContactEmail:
    def __init__(self, email, email2, email3):
        self.email = email
        self.email2 = email2
        self.email3 = email3

class ContactHomePage:
    def __init__(self, homepage):
        self.homepage = homepage

class ContactBDay:
    def __init__(self, bday, bmonth, byear):
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear

class ContactADay:
    def __init__(self, aday, amonth, ayear):
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear

class ContactSecInfo:
    def __init__(self, address2, phone2, notes):
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes