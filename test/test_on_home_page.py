import re
from model.contact import ContactMainInfo


def test_phones_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    contacts_on_home_page = app.contact.get_contact_list()
    for contact in contacts_on_home_page:
        contacts_on_home_page_db = db.get_contact_list_main_info(contact.id)
        assert contact.all_phones_from_home_page == contacts_on_home_page_db.all_phones_from_home_page


def test_email_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    contacts_on_home_page = app.contact.get_contact_list()
    for contact in contacts_on_home_page:
        contacts_on_home_page_db = db.get_contact_list_main_info(contact.id)
        assert contact.all_emails_from_home_page == contacts_on_home_page_db.all_emails_from_home_page


def test_first_name_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    contacts_on_home_page = app.contact.get_contact_list()
    for contact in contacts_on_home_page:
        contacts_on_home_page_db = db.get_contact_list_main_info(contact.id)
        assert contact.firstname == contacts_on_home_page_db.firstname


def test_last_name_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    contacts_on_home_page = app.contact.get_contact_list()
    for contact in contacts_on_home_page:
        contacts_on_home_page_db = db.get_contact_list_main_info(contact.id)
        assert contact.lastname == contacts_on_home_page_db.lastname


def test_phones_on_contact_view_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    contacts_on_home_page = app.contact.get_contact_list()
    for contact_list in contacts_on_home_page:
        app.contact.open_contact_to_edit_by_id(int(contact_list.id))
        contact_from_edit_page = app.contact.get_contact_info()
        app.contact.open_contact_page()
        contacts_on_home_page_db = db.get_contact_list_main_info(contact_list.id)
        assert contact_from_edit_page.lastname == contacts_on_home_page_db.lastname


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))