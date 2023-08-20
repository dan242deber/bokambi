from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def Retraites(request):
    return HttpResponse("Hello world! retraite")

def IndexR(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

