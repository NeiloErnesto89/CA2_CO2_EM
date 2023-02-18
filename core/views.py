from django.shortcuts import render


def home(request):
    return render(request, 'core/index.html')


def q1(request):
    return render(request, 'core/q1.html')