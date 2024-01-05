from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price',)
    success_url = reverse_lazy('catalog:products')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price',)
    success_url = reverse_lazy('catalog:products')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')
