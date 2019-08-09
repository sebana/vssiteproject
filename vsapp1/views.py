from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Person, Adjective
import csv
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def game(request):
        pos_people=[]
        just_people=[]
        neg_people=[]
        man=Person.objects.filter(gender=1).order_by('?')[:32]
        for i in man:
            if i.degree==1:
                pos_people.append(i)
            if i.degree==0:
                just_people.append(i)
            if i.degree==-1:
                neg_people.append(i)

        pos_adj=Adjective.objects.filter(degree=1).order_by('?')[:len(neg_people)]
        just_adj=Adjective.objects.filter(degree=0).order_by('?')[:len(just_people)]
        neg_adj=Adjective.objects.filter(degree=-1).order_by('?')[:len(pos_people)]

        pos=[]
        just=[]
        neg=[]   

        for i in pos_adj:
           pos.append(i.phrase)
        for i in just_adj:
           just.append(i.phrase)
        for i in neg_adj:
           neg.append(i.phrase)
        a=0   
        b=0
        c=0
        candidate=[]

        for i in man:
           if i.degree == -1:
              candidate.append([pos[a], i.name])
              a+=1
           if i.degree == 0:
              candidate.append([just[b], i.name])
              b+=1
           if i.degree == 1:
              candidate.append([neg[c], i.name])
              c+=1
        return render(request, 'game.html', {'candidate':candidate})

def result(request):
    return render(request, 'result.html')

def data_import():
    f = open('./person_data.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    for line in rdr:
        person = Person()
        person.name = rdr[0]
        person.gender = rdr[1]
        person.fav = 0 #영구적으로 통계자료 낼 때 쓰는거.
        person.image = ""
        person.degree = rdr[2]
        person.played = 0
        person.won = 0

"""
def worldcup(request) : #남성 32명을 뽑는 함수이다.
        pos_people=[]
        just_people=[]
        neg_people=[]
        man=Person.objects.filter(gender=1).order_by('?')[:32]
        for i in man:
            if i.degree==1:
                pos_people.append(i)
            if i.degree==0:
                just_people.append(i)
            if i.degree==-1:
                neg_people.append(i)
        
        pos_adj = random.sample(Adjective.objects.filter(gender = 1, degree = 1), len(neg_people)) #부정적인 남성의 수만큼 긍정적인 남성수식어를 뽑는다.
        just_adj = random.sample(Adjective.objects.filter(gender = 1, degree = 0), len(just_people)) #보통의 남성의 수만큼 보통의 남성수식어를 뽑는다.
        neg_adj = random.sample(Adjective.objects.filter(gender = 1, degree = 1), len(pos_people)) #긍정적인 남성의 수만큼 부정적인 남성수식어를 뽑는다.
        
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
        random.shuffle(candidate)
        real_candidate=[]
        for i in range(0,16):
                real_candidate.append([candidate[i*2],candidate[i*2+1]]) #이 행위를 통해 32강의 대진표가 완성되게 된다.
        return render(request, 'game.html', {'real_candidate':real_candidate}) #candidate는 ['도박하는 박보검', '10억 버는 김제동' ... ]의 31까지의 인덱스를 가진 리스트이다.
"""
#포스트를 사용해서 16개의 인자를 받는다.

def result(request):
    return render(request, 'result.html')

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

#일단 candidate를 통해서 32개의 인자를 가진 리스트를 만드는 데에는 성공했지만 그 다음 투표를 진행시킬 때 새 함수를 짜야 하는데
#그런데 그 새 함수에서 candidate라는 말을 사용할 수 없게 된다. 왜냐하면 모델에 저장되어 있지 않기 때문이다.

def vote(request) :
        league = 32
        votelist=[]
        votelist.append(request.POST['winner'])
        return redirect('/')
