from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2_first(request):
    return HttpResponse('<h1>This is the first view of app2</h1>')

def app2_SECOND(request):
    return HttpResponse('<h2> This is the second view of app2</h2>')
