from django.shortcuts import render, get_object_or_404
from DjangoDemo.settings import STATIC_URL
from .models import Work, Study, UserInfo, Organization, EducationalOrganization


def staticfiles(request):
    return {'STATIC': STATIC_URL}


def home(request):
    data = UserInfo.objects.get(id=1)
    data.hobbies = data.hobbies.all()
    return render(request, 'index.html',
                  {'info': data, 'hobbies': data.hobbies.all()})


def work(request, limit=None):
    if limit:
        limit = int(limit)
    return render(request, 'work.html', {'title': 'Информация об опыте работы',
        'works': Work.objects.all()[:limit]})


def work_detail(request, id):
    return render(request, 'work_detail.html', {'title': 'Информация об организации',
        'organization': get_object_or_404(Organization, id=id)
                                                })


def study(request):
    return render(request, 'study.html', {'title': 'Информация о квалификации',
        'studies': Study.objects.all()})


def study_detail(request, id):
    return render(request, 'study_detail.html', {'title': 'Информация об учебном заведение',
        'study': get_object_or_404(EducationalOrganization, id=id)
                                                })
