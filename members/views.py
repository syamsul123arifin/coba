from django.shortcuts import render
from django. http import HttpResponse
from django.template import loader


def trainer(request):
    template = loader.get_template('trainer.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def why(request):
    template = loader.get_template('why.html')
    return HttpResponse(template.render())

def members(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())



# Create your views here.
