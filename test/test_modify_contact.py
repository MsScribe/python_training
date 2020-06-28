from model.contact import ContactMainInfo
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(firstname="1", middlename="2", lastname="3", nickname="4", title="5", company="6", homeaddress="7", homephone="", mobilephone="", workphone="333", faxphone="35677", email="1dad23qwert@test.ru", email2="1dad234qwsa@test.com", email3="111test123@test.ru", homepage="hhtps://21test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="3", phone2="4", notes="5")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(firstname="First Name Test")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(middlename="Middle Name Test")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    contact.firstname = old_contacts[index].firstname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(lastname="Last Name Test")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)


def test_modify_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(nickname="NickName Test")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    contact.firstname = old_contacts[index].firstname
    contact.lastname = old_contacts[index].lastname
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)