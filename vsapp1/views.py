from django.shortcuts import render
from .models import Person, Adjective
import csv
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def game(request):
<<<<<<< HEAD
=======
    return render(request, 'game.html')

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

def worldcup(request) : #남성 32명을 뽑는 함수이다.
>>>>>>> cf95179de86c1bfde372e2356fccb421029cef6d
        all_people = Person.objects.filter(gender = request.POST['choice']) #남성을 전부 받는다.
        people = random.sample(all_people, 32) #받은 남성 중에 32명을 뽑는다.                
        pos_people = people.objects.filter(degree = 1) #긍정적인 남성
        just_people = people.objects.filter(degree = 0) #보통의 남성
        neg_people = people.objects.filter(degree = -1) #부정적인 남성
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
                league=32
        while league!=1:
                if league==32:
                        real_candidate16=[]
                        candidate16=[]
                        candidate16.append(request.POST['winner'])
                        random.shuffle(candidate16)
                        for i in range(0,8):
                                real_candidate16.append([candidate16[i*2],candidate16[i*2+1]])
                        league=16
                if league==16:
                        real_candidate8=[]
                        candidate8=[]
                        candidate8.append(request.POST['winner'])
                        random.shuffle(candidate8)
                        for i in range(0,4):
                                real_candidate8.append([candidate8[i*2],candidate8[i*2+1]])
                        league=8
                if league==8:
                        real_candidate4=[]
                        candidate4=[]
                        candidate4.append(request.POST['winner'])
                        random.shuffle(candidate4)
                        for i in range(0,4):
                                real_candidate4.append([candidate4[i*2],candidate4[i*2+1]])
                        league=4
                if league==4:
                        real_candidate2=[]
                        candidate2=[]
                        candidate2.append(request.POST['winner'])
                        random.shuffle(candidate2)
                        for i in range(0,2):
                                real_candidate2.append([candidate2[i*2],candidate2[i*2+1]])
                        league=2
                if league==2:
                        real_candidate1=[]
                        candidate1=[]
                        candidate1.append(request.POST['winner'])
                        random.shuffle(candidate1)
                        for i in range(0,1):
                                real_candidate1.append([candidate2[i*2],candidate2[i*2+1]])
                        league=1
                        
        return render(request, 'game.html', {'real_candidate':real_candidate}) #candidate는 ['도박하는 박보검', '10억 버는 김제동' ... ]의 31까지의 인덱스를 가진 리스트이다.

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
