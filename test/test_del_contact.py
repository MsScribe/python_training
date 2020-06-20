from model.group import Group
from model.contact import ContactMainInfo


def test_delete_first_group(app):
    if app.contact.count() == 0:
        app.contact.create(ContactMainInfo(firstname="TestFirstName"))
    app.contact.delete_first_contact()