from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogEntryDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, HomeListView


app_name = BlogConfig.name

urlpatterns = [
    path('blog/', HomeListView.as_view(), name='blog'),
    path('blog_entry/<int:pk>/', BlogEntryDetailView.as_view(), name='blogentry'),
    path('blog_form/new/', BlogCreateView.as_view(), name='blogform'),
    path('blog_form/<int:pk>/edit/', BlogUpdateView.as_view(), name='blogform_edit'),
    path('blog_confirm/<int:pk>/delete/', BlogDeleteView.as_view(), name='blogconfirm_delete'),
]