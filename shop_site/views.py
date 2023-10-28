from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator


class Index(TemplateView):
    template_name = 'index.html'  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['category'] = Category.objects.all()

        category = Category.objects.all()[:6]

        for index, value in enumerate(category):
            products = Products.objects.filter(categoryObject=value)[:10]
            category[index].products = products

        context['category'] = category


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

def productDetails(request, id):
    row = Products.objects.get(id=id)
    images = ProductsImages.objects.filter(productObject = row)
    context = {
        "row":row, 
        'images':images
    }
    return render(request, "product-details.html", context)

def blogDetails(request, id):
    row = Blogs.objects.get(id=id)
    context = {
        "row":row
    }
    return render(request, "blog-details.html", context)


def shopPage(request):

    begin_price = 0
    end_price = 1000000

    if request.GET.get('begin_price'):
        begin_price = request.GET.get('begin_price')
    if request.GET.get('end_price'):
        end_price = request.GET.get('end_price')


    search = ""
    if request.GET.get('search'):
        search = request.GET.get('search')

    page = 1
    if request.GET.get('page'):
        page = int(request.GET.get('page'))

    rows = Products.objects.all().filter(name__contains=search, price__range=(begin_price, end_price))
    paginator = Paginator(rows, 15)

    next_page = page + 1 if (page + 1) <= len(paginator.page_range) else page
    previous_page = page - 1 if (page - 1) != 0 else page


    brands = Brands.objects.all()

    context = {
        "brands":brands,
        'result_count': f"Показано {15} из {len(rows)}",
        'products': paginator.page(page),
        'pages': paginator.page_range,
        'current_page':page,
        'next_page':next_page,
        'previous_page':previous_page,
    }
    return render(request, "shop.html", context)

