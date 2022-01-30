from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'manuals/index.html')


def home(request):
    return render(request, 'manuals/home.html')


def home_topic(request, topic: str):
    if topic == 'mi-stick':
        return render(request, f'manuals/mi-stick.html')
    else:
        return HttpResponseNotFound('<h1>Пока такой инструкции нет<h1>')


def dacha(request):
    return render(request, 'manuals/dacha.html')


def dacha_topic(request, topic: str):
    return render(request, 'manuals/generator.html')
