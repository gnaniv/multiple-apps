from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def app1_first(request):
    return HttpResponse('<h1>First view of app1</h1>')

def app1_second(request):
    return HttpResponse('<h2> second view of app1</h2>')
