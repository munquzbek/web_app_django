from django.shortcuts import render
from django.views.generic import ListView, DetailView

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

# Function Based View
# def products(request):
#     product_list = Product.objects.all()
#     context = {
#         'product_list': product_list,
#         'title': 'Products page'
#     }
#     return render(request, 'catalog/product_list.html', context)


# Class Based View the same as 'def products(request):' (previous function)
class ProductListView(ListView):
    model = Product

# FBV
# def product(request, pk):
# GET request
#     product = Product.objects.get(pk=pk)
#     context = {
#         'product': product
#     }
#     return render(request, 'catalog/product_detail.html', context)


# CBV
class ProductDetailView(DetailView):
    model = Product

