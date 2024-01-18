from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contact, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, category_list

from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    # products
    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    # categories
    path('categories/', cache_page(60)(category_list), name='list_category'),
]
