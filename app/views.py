from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.

QUESTIONS = [
        {
            'id' : i,
            'title' : f'Question {i}',
            'content' : 'Take me to church' +
        'I ll worship like a dog at the shrine of your lies' +
        'I ll tell you my sins and you can sharpen your knife' +
        'Offer me that deathless death' +
        'Good God, let me give you my life' +
        'Take me to church' +
        'I ll worship like a dog at the shrine of your lies' +
        'I ll tell you my sins and you can sharpen your knife' +
        'Offer me that deathless death' +
        f'Good God, let me give you my life {i}'
        } for i in range (20)
    ]

def paginate(objects, page, per_page=7):
    paginator = Paginator(objects, per_page=per_page)

    return paginator.page(page)

def index(request):
    page = request.GET.get('page', 1)
    return render(request, 'index.html', context={'questions' : paginate(QUESTIONS, page=page), 'page' : page })

def login(request):
    return render(request, 'login.html')

def question(request, question_id):
    item = QUESTIONS[question_id]
    answers = [
        {
            'id' : i,
            'content' : f'Take me to church' +
        'I ll worship like a dog at the shrine of your lies' +
        'I ll tell you my sins and you can sharpen your knife' +
        'Offer me that deathless death' +
        'Good God, let me give you my life' +
        'Take me to church' +
        'I ll worship like a dog at the shrine of your lies' +
        'I ll tell you my sins and you can sharpen your knife' +
        'Offer me that deathless death' +
        'Good God, let me give you my life {i}'
        } for i in range (3)
    ]
    return render(request, 'question.html', {'question' : item, 'answers': answers})

def tag(request):
    return render(request, 'tag.html')

def signup(request):
    return render(request, 'signup.html')

def ask(request):
    return render(request, 'ask.html')