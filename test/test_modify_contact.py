from model.contact import ContactMainInfo


def test_modify_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(firstname="1", middlename="2", lastname="3", nickname="4", title="5", company="6", homeaddress="7", homephone="", mobilephone="", workphone="333", faxphone="35677", email="1dad23qwert@test.ru", email2="1dad234qwsa@test.com", email3="111test123@test.ru", homepage="hhtps://21test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="3", phone2="4", notes="5")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)


def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(firstname="First Name Test")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)


def test_modify_contact_middlename(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(middlename="Middle Name Test")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    contact.firstname = old_contacts[0].firstname
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)


def test_modify_contact_lastname(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(lastname="Last Name Test")
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)


def test_modify_contact_nickname(app):
    old_contacts = app.contact.get_contact_list()
    contact = ContactMainInfo(nickname="NickName Test")
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    contact.lastname = old_contacts[0].lastname
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)