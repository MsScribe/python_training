from pytest_bdd import scenario
from .contact_step import *


@scenario('contacts.feature', 'Add new contact')
def test_add_contact():
    pass


@scenario('contacts.feature', 'Modify a contact')
def test_modify_contact():
    pass


@scenario('contacts.feature', 'Delete a contact')
def test_delete_contact():
    pass