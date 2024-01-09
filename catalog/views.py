from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductCreateForm, VersionForm
from catalog.models import Product, Version


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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['versions'] = Version.objects.filter(product=self.object)
        return context_data


class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy('catalog:products')
    form_class = ProductCreateForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Formset
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST)
        else:
            context_data['formset'] = VersionFormset()

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        user = self.request.user
        self.object.user = user

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    success_url = reverse_lazy('catalog:products')
    form_class = ProductCreateForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Formset
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products')
