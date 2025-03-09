from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactsTemplateView, ProductDeleteView, ProductCreateView, ProductDetailView, \
    ProductUpdateView, ProductsByCategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60*15)(ProductDetailView.as_view()), name="product"),
    path('home/product/new/', ProductCreateView.as_view(), name="product_new"),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name="product_edit"),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
    path('product/category/', ProductsByCategoryListView.as_view(), name="products_by_category"),
]
