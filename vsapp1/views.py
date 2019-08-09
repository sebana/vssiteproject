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

def worldcup(request) : #남성 32명을 뽑는 함수이다.
        all_people = Person.objects.filter(gender = request.POST['choice']) #남성을 전부 받는다.
        people = random.sample(all_people, 32) #받은 남성 중에 32명을 뽑는다.                
        pos_people = people.objects.filter(degree = 1) #긍정적인 남성
        just_people = people.objects.filter(degree = 0) #보통의 남성
        neg_people = people.objects.filter(degree = -1). #부정적인 남성
        pos_adj = random.sample(Adjectives.objects.filter(gender = 1, degree = 1), len(neg_people)) #부정적인 남성의 수만큼 긍정적인 남성수식어를 뽑는다.
        just_adj = random.sample(Adjectives.objects.filter(gender = 1, degree = 0), len(just_people)) #보통의 남성의 수만큼 보통의 남성수식어를 뽑는다.
        neg_adj = random.sample(Adjectives.objects.filter(gender = 1, degree = 1), len(pos_people)) #긍정적인 남성의 수만큼 부정적인 남성수식어를 뽑는다.
        candidate = []
        pospeople=[]
        negpeople=[]
        justpeople=[]
        posadj=[]
        justadj=[]
        negadj=[]
        for i in pos_people :
                pospeople.append(i.name)
        for i in just_people :
                justpeople.append(i.name)
        for i in neg_people :
                negpeople.append(i.name)
        for i in pos_adj :
                posadj.append(i.name)
        for i in just_adj :
                justadj.append(i.name)
        for i in neg_adj :
                negadj.append(i.name)
        for i in pospeople:
                a=random.choice(negadj)
                candidate.append(a+i)
                negadj.remove(a)
        for i in justpeople:
                a=random.choice(justadj)
                candidate.append(a+i)
                justadj.remove(a)
        for i in negpeople:
                a=random.choice(posadj)
                candidate.append(a+i)
                posadj.remove(a)
        return render(request, '월드컵 url', {'candidate':candidate})
                #candidate는 ['도박하는 박보검', '10억 버는 김제동' ... ]의 31까지의 인덱스를 가진 리스트이다.

#일단 candidate를 통해서 32개의 인자를 가진 리스트를 만드는 데에는 성공했지만 그 다음 투표를 진행시킬 때 새 함수를 짜야 하는데
#그런데 그 새 함수에서 candidate라는 말을 사용할 수 없게 된다. 왜냐하면 모델에 저장되어 있지 않기 때문이다.
