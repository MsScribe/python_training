from model.contact import ContactMainInfo
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="TestFirstName"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)