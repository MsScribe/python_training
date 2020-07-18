# -*- coding: utf-8 -*-
from model.contact import ContactMainInfo


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