from fixture.orm import ORMFixture
from model.group import Group
from model.contact import ContactMainInfo
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    group_list = db.get_group_list()
    # group_id = random.choice(group_list)
    for group_id in group_list:
        l = db.get_groups_not_in_contact(Group(id=group_id.id))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()