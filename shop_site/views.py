from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

class Index(TemplateView):
    template_name = 'index.html'  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products'] = Products.objects.all()
        context['category'] = Category.objects.all()

        return context



class ContactViews(CreateView):
    model = Contacts
    template_name = 'contact.html'
    fields = ['firstname', 'lastname', 'number', 'email', 'message']

def about(request):
    workers = Workers.objects.all()
    reviews = Reviews.objects.all()[:8]

    context = {
        'workers':workers,
        'reviews':reviews,
    }
    return render(request, "about.html", context)

def blogs(request):
    rows = Blogs.objects.all()
    context = {
        'rows':rows
    }
    return render(request, 'blog.html', context)