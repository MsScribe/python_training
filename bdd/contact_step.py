from pytest_bdd import given, when, then
from model.contact import ContactMainInfo
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <middlename>, <lastname>, <nickname>, <title>, <company>, <homeaddress>, <homephone>, <mobilephone>, <workphone>, <faxphone>, <email>, <email2>, <email3>, <homepage>, <bday>, <bmonth>, <byear>, <aday>, <amonth>, <ayear>, <address2>, <phone2> and <notes>')
def new_contact(firstname, middlename, lastname, nickname, title, company, homeaddress, homephone, mobilephone, workphone, faxphone, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes):
    return ContactMainInfo(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title, company=company, homeaddress=homeaddress, homephone=homephone, mobilephone=mobilephone, workphone=workphone, faxphone=faxphone,email=email, email2=email2, email3=email3, homepage=homepage, bday=bday, bmonth=bmonth, byear=byear, aday=aday, amonth=amonth, ayear=ayear, address2=address2, phone2=phone2, notes=notes)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(db, app, check_ui, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I modify the contact from the list')
def modify_contact(app, random_contact):
    app.contact.modify_contact_by_id(random_contact.id, random_contact)


@then('the contact has been replaced in the contact list')
def verify_contact(non_empty_contact_list, db, app, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(db.get_contact_list())
    old_contacts[old_contacts.index(random_contact)].firstname = random_contact.firstname
    old_contacts[old_contacts.index(random_contact)].lastname = random_contact.lastname
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old contact list without the deleted contact')
def verify_contact_deleted(db, app, non_empty_contact_list, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)