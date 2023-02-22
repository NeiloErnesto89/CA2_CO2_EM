from django.shortcuts import render
from core.Services import *

def home(request):
    return render(request, 'core/index.html')

def q1(request):
    return render(request, 'core/q1.html')

def q2(request):
    return render(request, 'core/q2.html')

def q3(request):
    return render(request, 'core/q3.html')

def q4(request):
    return render(request, 'core/q4.html')

def q5(request):
    return render(request, 'core/q5.html')

def q6(request):
    return render(request, 'core/q6.html')

def q7(request):
    return render(request, 'core/q7.html')