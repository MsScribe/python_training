# -*- coding: utf-8 -*-
from model.contact import ContactMainInfo
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_dijits(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@mail.ru"


testdata = [ContactMainInfo(firstname=random_string("firstname", 15), middlename=random_string("middlename", 15), lastname=random_string("lastname", 15), nickname=random_string("nickname", 10), title=random_string("title", 20), company=random_string("company", 25), homeaddress=random_string("homeaddress", 20), homephone=random_dijits("+", 11), mobilephone=random_dijits("+", 11), workphone=random_dijits("+", 15), faxphone=random_dijits("+", 7), email=random_email("email", 5), email2=random_email("email", 5), email3=random_email("email", 5), homepage=random_string("https://", 15), bday="1", bmonth="July", byear="1990", aday="6", amonth="November", ayear="1987", address2=random_string("address2", 25), phone2=random_dijits("+", 11), notes=random_string("notes", 30))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.open_home_page()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)