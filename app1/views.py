from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def display(request):
	return HttpResponse("<h1>Hola Mundo!</h1>")

def displayDateTime(request):
	dt = datetime.datetime.now()
	s= "<h1>Texto" + str(dt)
	return HttpResponse(s)

