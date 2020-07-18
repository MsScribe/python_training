from model.contact import ContactMainInfo
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    contact = ContactMainInfo(firstname="1", middlename="2", lastname="3", nickname="4", title="5", company="6", homeaddress="7", homephone="", mobilephone="", workphone="333", faxphone="35677", email="1dad23qwert@test.ru", email2="1dad234qwsa@test.com", email3="111test123@test.ru", homepage="hhtps://21test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="3", phone2="4", notes="5")
    app.contact.modify_contact_by_id(contact_random.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(db.get_contact_list())
    old_contacts[old_contacts.index(contact_random)].firstname = contact.firstname
    old_contacts[old_contacts.index(contact_random)].lastname = contact.lastname
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    contact = ContactMainInfo(firstname="First Name Test")
    app.contact.modify_contact_by_id(contact_random.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(db.get_contact_list())
    old_contacts[old_contacts.index(contact_random)].firstname = contact.firstname
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)


def test_modify_contact_middlename(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    contact = ContactMainInfo(middlename="Middle Name Test")
    app.contact.modify_contact_by_id(contact_random.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(db.get_contact_list())
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)


def test_modify_contact_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    contact = ContactMainInfo(lastname="Last Name Test")
    app.contact.modify_contact_by_id(contact_random.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(db.get_contact_list())
    old_contacts[old_contacts.index(contact_random)].lastname = contact.lastname
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)


def test_modify_contact_nickname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = db.get_contact_list()
    contact_random = random.choice(old_contacts)
    contact = ContactMainInfo(nickname="NickName Test")
    app.contact.modify_contact_by_id(contact_random.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(db.get_contact_list())
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)