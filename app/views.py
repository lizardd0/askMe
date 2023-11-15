from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from app.models import *

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
    content = paginate(request, Question.objects.all())
    tags = Tag.objects.popular_tags()
    return render(request, 'index.html', context={'questions' : content, 'tags' : tags})

def hot(request):
    content = paginate(request, Question.objects.hot())
    tags = Tag.objects.popular_tags()
    return render(request, 'index.html', context={'questions' : content, 'tags' : tags})


def login(request):
    tags = Tag.objects.popular_tags()
    return render(request, 'login.html', {'tags' : tags})

def question(request, question_id):
    tags = Tag.objects.popular_tags()
    item = Question.objects.get(id=question_id)
    # answers = [
    #     {
    #         'id' : i,
    #         'content' : f'Take me to church' +
    #     'I ll worship like a dog at the shrine of your lies' +
    #     'I ll tell you my sins and you can sharpen your knife' +
    #     'Offer me that deathless death' +
    #     'Good God, let me give you my life' +
    #     'Take me to church' +
    #     'I ll worship like a dog at the shrine of your lies' +
    #     'I ll tell you my sins and you can sharpen your knife' +
    #     'Offer me that deathless death' +
    #     f'Good God, let me give you my life {i}'
    #     } for i in range (3)
    # ]
    answers = paginate(request, Answer.objects.by_question(question_id), per_page=3)
    return render(request, 'question.html', {'question' : item, 'answers': answers, 'tags' : tags})

def tag(request, tag_name):
    content = paginate(request,Question.objects.by_tag(tag_name))
    tags = Tag.objects.popular_tags()
    return render(request, 'tag.html', {'questions' : content, 'tag' : tag_name, 'tags' : tags})

def signup(request):
    tags = Tag.objects.popular_tags()
    return render(request, 'signup.html', {'tags' : tags})

def ask(request):
    tags = Tag.objects.popular_tags()
    return render(request, 'ask.html', {'tags' : tags})

def settings(request):
    tags = Tag.objects.popular_tags()
    return render(request, 'settings.html', {'tags' : tags})