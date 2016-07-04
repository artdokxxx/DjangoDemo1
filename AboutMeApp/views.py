from django.shortcuts import render
from DjangoDemo.settings import STATIC_URL
from .models import Work, Study, UserInfo


def staticfiles(request):
    return {'STATIC': STATIC_URL}


def home(request):
    data = UserInfo.objects.get(id=1)
    data.hobbies = data.hobbies.all()
    return render(request, 'index.html',
                  {'info': data, 'hobbies': data.hobbies.all()})


def work(request):
    return render(request, 'work.html', {'title': 'Информация об опыте работы',
        'works': Work.objects.all()})


def study(request):
    return render(request, 'study.html', {'title': 'Информация о квалификации',
        'studies': Study.objects.all()})
