from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'title': 'Home page'
    }
    return render(request, 'catalog/home.html', context)


def contact(request):
    context = {
        'title': 'Contact page'
    }
    return render(request, 'catalog/contact.html', context)


def products(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
        'title': 'Products page'
    }
    return render(request, 'catalog/products.html', context)
