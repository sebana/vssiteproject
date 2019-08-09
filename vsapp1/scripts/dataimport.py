
import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from manage import DEFAULT_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", DEFAULT_SETTINGS_MODULE)

import django
django.setup() 

from vsapp1.models import Person
f = open('data_person.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

# for line in rdr:
#     person = Person()
#     person.name = rdr[0]
#     person.gender = rdr[1]
#     person.fav = 0
#     person.image = ""
#     person.degree = rdr[2]
#     person.played = 0
#     person.won = 0

# def run():
#     import csv
#     from vsapp1.models import Person
#     f = open('data_person.csv', 'r', encoding='utf-8')
#     rdr = csv.reader(f)
#     print("success")
