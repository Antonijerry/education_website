from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def basepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def home_page(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def about_page(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def contact_page(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

