from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ContactsTemplateView, ProductInfoDetailView, HomeListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_info/<int:pk>/', ProductInfoDetailView.as_view(), name='product_info'),
]
