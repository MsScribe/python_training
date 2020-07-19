from fixture.orm import ORMFixture
from model.group import Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    group_list = db.get_group_list()
    group_id = random.choice(group_list)
    l = db.get_contacts_in_group(Group(id=group_id.id))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()