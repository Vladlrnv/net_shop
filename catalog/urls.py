from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home

app = CatalogConfig.name

urlpatterns = [
    path('', home, name='home')
]