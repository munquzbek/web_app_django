from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, products, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('product/<int:pk>', product, name='product'),
]
