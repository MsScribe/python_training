from model.group import Group
from model.contact import ContactMainInfo


def test_delete_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="TestFirstName"))
    app.contact.delete_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert sorted(old_contacts, key=ContactMainInfo.id_or_max) == sorted(new_contacts, key=ContactMainInfo.id_or_max)