from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

class Index(TemplateView):
    template_name = 'index.html'  

class ContactViews(CreateView):
    model = Contacts
    template_name = 'contact.html'
    fields = ['firstname', 'lastname', 'number', 'email', 'message']
