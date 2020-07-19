from model.contact import ContactMainInfo
from model.group import Group
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(ContactMainInfo(firstname="TestFirstName"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=ContactMainInfo.id_or_max) == sorted(app.contact.get_contact_list(), key=ContactMainInfo.id_or_max)


def test_delete_contact_in_group(app, db):
    # Получить список контактов в группе
    old_contacts_in_group = db.get_contacts_in_groups_list()
    group_list = db.get_group_list()
    contact = ContactMainInfo(firstname="FirstNameTest", middlename="MiddleNameTest", lastname="LastNameTest", nickname="NickNameTest", title="TestTitle", company="TestCompany", homeaddress="Test Street Test home", homephone="9998887766", mobilephone="+79876543210", workphone="+567", faxphone="3456", email="123qwert@test.ru", email2="1234qwsa@test.com", email3="test123@test.ru", homepage="hhtps://test.ru", bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2="Street address", phone2="testhome", notes="blablabla")
    # Проверяем, есть ли привязанные контакты к группе. Если нет, добавляем
    if len(old_contacts_in_group) == 0:
        app.open_home_page()
        # Проверяем, есть ли вообще группы, если нет, добавляем
        if len(group_list) == 0:
            app.group.create(Group(name="TestName", header="TestHeader", footer="TestFooter"))
            group_list = db.get_group_list()
        group_name = random.choice(group_list)
        app.contact.create_in_group(contact, group_name.name)
        old_contacts_in_group = db.get_contacts_in_groups_list()
    # Выбрать группу, которая привязана к контакту
    select_group_in_contact_id = old_contacts_in_group[-1].group_id
    select_group_in_contact = old_contacts_in_group[-1]
    # Удалить группу
    app.group.delete_group_by_id(select_group_in_contact_id)
    # Сравнить
    old_contacts_in_group.remove(select_group_in_contact)
    new_contacts_in_group = db.get_contacts_in_groups_list()
    assert (old_contacts_in_group == new_contacts_in_group)