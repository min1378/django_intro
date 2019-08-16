#pages/views.py
from django.shortcuts import render
from datetime import datetime
import random
# Create your views here.
def index(request): #첫번째 인자는 반드시 request => 사용자가 보내는 요청에 대한 정보
    return render(request, 'index.html') #render의 첫번째 인자도 반드시 request


def introduce(request):
    return render(request, 'introduce.html')


def dinner(request, name):
    menu = ['강남 더막창스', '강남 노랑통닭', '강남 땀땀', '강남 타이거슈가']
    pick = random.choice(menu)
    context = {
        'pick': pick,
        'name': name
    }
    return render(request, 'dinner.html', context)

def image(request):
    # image url을 context에 담아서 image.html에 전달한다.
    images = ['https://t1.daumcdn.net/cfile/tistory/995499415BA82B591F',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT71hMyCz1byrLDf6hW7ZKlfl2eLrIRi6UuxTmEIimStMHyeR9B',
    ]
    pick = random.choice(images)
    context ={
        'pick' : pick
    }  

    return render(request, 'image.html', context)

def greeting(request, name):
    context = {
        'name' : name
    }
    return render(request, 'greeting.html', context)

def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result
    }
    return render(request, 'times.html', context)


def template_language(request):
    menus = ['짜장면', '짬뽕', '양장피', '탕수육']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'mango', 'cucumber', 'banana']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus' : menus,
        'my_sentence' : my_sentence,
        'messages': messages,
        'empty_list' : empty_list,
        'datetimenow' : datetimenow,
    }
    return render(request,'template_language.html', context)


def info(request):

    return render(request, 'info.html')



def student(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'student.html', context)

def isbirthday(request):

    return render(request, 'isbirthday.html')

def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42] #870회차 로또
    lottos = []
    result = '응 아니야!'
    number = list(range(1,46))
    while len(lottos) < 6:
        num = random.choice(number)
        if not num in lottos:
            lottos.append(num)
    lottos = sorted(lottos)
    if lottos == real_lotto :
        result = '당첨!!!!!!!!!!!!!!!!!!!!'
    context = {
        'lottos' : lottos,
        'real_lotto' : real_lotto,
        'result' : result

    }
    return render(request, 'lotto.html', context)