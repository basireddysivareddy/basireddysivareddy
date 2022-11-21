from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse('I don`t know who r u')

def second(request):
    return HttpResponse('<marquee bgcolor=green>myself basireddy sivashankar reddy</marquee>')

def third(request):
    return HttpResponse('<h1>I love U deepa</h1>')