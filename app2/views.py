from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def perrito(request):
    return HttpResponse('<br><h1> Este es un perrito</h1><br><br><h2>Hola Wapo</h2>')

