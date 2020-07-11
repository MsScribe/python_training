from model.contact import ContactMainInfo
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


# Дефолтные значения
n = 5
f = "data/contacts.json"


# o - Название опции
for o, a in opts:
    if o == "-f":
        f = a
    elif o == "-n":
        n = int(a)


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


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
print("Path: " + f + " , " + file)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))