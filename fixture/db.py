import pymysql.cursors
from model.group import Group
from model.contact import ContactMainInfo
from model.contact_in_group import ContactInGroup
import re


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(ContactMainInfo(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_list_main_info(self, id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select firstname, lastname, id, home, mobile, work, phone2, email, email2, email3 from addressbook where id='%s'" % id)
            for row in cursor:
                (firstname, lastname, id, home, mobile, work, phone2, email, email2, email3) = row
                list.append(ContactMainInfo(firstname=firstname, lastname=lastname, id=str(id), all_phones_from_home_page=clear(merge_phones_like_on_home_page([home, mobile, work, phone2])), all_emails_from_home_page=clear(merge_emails_like_on_home_page([email, email2, email3]))))
        finally:
            cursor.close()
        return list[0]

    def destroy(self):
        self.connection.close()

    def get_contacts_in_groups_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append(ContactInGroup(id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return list

    def get_groups_not_in_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("(SELECT gr.group_id, gr.group_name, gr.group_header, gr.group_footer FROM group_list gr LEFT OUTER JOIN address_in_groups adingr ON gr.group_id=adingr.group_id WHERE adingr.group_id is NULL) UNION ALL (SELECT gr.group_id, gr.group_name, gr.group_header, gr.group_footer FROM group_list gr RIGHT OUTER JOIN address_in_groups adingr ON gr.group_id=adingr.group_id WHERE gr.group_id is NULL)")
            for row in cursor:
                (group_id, name, header, footer) = row
                list.append(Group(id=str(group_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_not_in_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("(SELECT c.id, c.firstname, c.lastname FROM addressbook c LEFT OUTER JOIN address_in_groups adingr ON c.id=adingr.id WHERE adingr.id is NULL) UNION ALL (SELECT c.id, c.firstname, c.lastname FROM addressbook c RIGHT OUTER JOIN address_in_groups adingr ON c.id=adingr.id WHERE c.id is NULL)")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(ContactMainInfo(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

def clear(s):
    return re.sub("[() - \n]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, contact))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, contact))))