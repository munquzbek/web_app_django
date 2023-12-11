from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
]
