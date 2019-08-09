
import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vsproject.settings')

import django
django.setup() 

from vsapp1.models import Person
f = open('vsapp1/scripts/data_person.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    person = Person()
    person.name = line[0]
    person.gender = int(line[1])
    person.fav = 0
    person.image = ""
    person.degree = int(line[2])
    person.played = 0
    person.won = 0
    person.save()

# def run():
#     import csv
#     from vsapp1.models import Person
#     f = open('data_person.csv', 'r', encoding='utf-8')
#     rdr = csv.reader(f)
#     print("success")
