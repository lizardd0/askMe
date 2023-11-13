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

TAGS = ["python", "css", "Java", "IOS"]

def paginate(request, objects, per_page=7):
    paginator = Paginator(objects, per_page=per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def index(request):
    content = paginate(request, QUESTIONS)
    return render(request, 'index.html', context={'questions' : content, 'tags' : TAGS})

def hot(request):
    content = paginate(request, QUESTIONS)
    return render(request, 'index.html', context={'questions' : content, 'tags' : TAGS})


def login(request):
    return render(request, 'login.html', {'tags' : TAGS})

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
        f'Good God, let me give you my life {i}'
        } for i in range (3)
    ]
    return render(request, 'question.html', {'question' : item, 'answers': answers, 'tags' : TAGS})

def tag(request, tag_name):
    content = paginate(request, QUESTIONS)
    return render(request, 'tag.html', {'questions' : content, 'tag' : tag_name, 'tags' : TAGS})

def signup(request):
    return render(request, 'signup.html', {'tags' : TAGS})

def ask(request):
    return render(request, 'ask.html', {'tags' : TAGS})

def settings(request):
    return render(request, 'settings.html', {'tags' : TAGS})