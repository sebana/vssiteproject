
import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vsproject.settings')

import django
django.setup() 

from vsapp1.models import Person
from vsapp1.models import Adjective

#사람 임포트
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


#수식어 임포트
f = open('vsapp1/scripts/adjectives_import_man.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    adjective = Adjective()
    adjective.phrase = line[0]
    adjective.gender = 1
    adjective.degree = line[1]
    adjective.played = 0
    adjective.won = 0

f = open('vsapp1/scripts/adjectives_import_women.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    adjective = Adjective()
    adjective.phrase = line[0]
    adjective.gender = 2
    adjective.degree = line[1]
    adjective.played = 0
    adjective.won = 0