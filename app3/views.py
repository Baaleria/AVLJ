from django.shortcuts import render
from django.http import HttpResponse

def Inicio(request):
    return HttpResponse("<h1>Estas viendo la APP3!!</h1>")