# -*- coding: utf-8 -*-
from model.contact import ContactMainInfo
from model.group import Group
from model.contact_in_group import ContactInGroup
import random


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.open_home_page()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)


def test_add_contact_in_group(app, db, check_ui):
    # Получить список групп
    group_list = db.get_group_list()
    contact = ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla")
    # Создать группу если групп нет
    if len(group_list) == 0:
        app.group.create(Group(name="TestName", header="TestHeader", footer="TestFooter"))
        group_list = db.get_group_list()
    # Выбрать рандомную группу
    group_name = random.choice(group_list)
    old_contacts = db.get_contact_list()
    old_contacts_in_group = db.get_contacts_in_groups_list()
    # Добавление контакта
    app.open_home_page()
    app.contact.create_in_group(contact, group_name.name)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)
    old_contacts_in_group.append(ContactInGroup(id=new_contacts[-1].id, group_id=group_name.id))
    assert sorted(db.get_contacts_in_groups_list(), key=ContactInGroup.id_or_max) == sorted(old_contacts_in_group, key=ContactInGroup.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)