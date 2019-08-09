from django.shortcuts import render
from .models import Person
import csv

# Create your views here.

def home(request):
    return render(request, 'home.html')

def data_import():
    f = open('./person_data.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    for line in rdr:
        person = Person()
        person.name = rdr[0]
        person.gender = rdr[1]
        person.fav = 0
        person.image = ""
        person.degree = rdr[2]
        person.played = 0
        person.won = 0