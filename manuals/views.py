from django.shortcuts import render


def index(request):
    return render(request, 'manuals/index.html')


def home(request):
    return render(request, 'manuals/home.html')


def dacha(request):
    return render(request, 'manuals/dacha.html')
