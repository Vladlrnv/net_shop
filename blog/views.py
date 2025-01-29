from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from blog.models import BlogEntry


class BlogCreateView(CreateView):
    model = BlogEntry
    fields = ['header', 'content', 'preview']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('home.html')


class BlogUpdateView(UpdateView):
    model = BlogEntry
    fields = ['header', 'content', 'preview']
    template_name = 'blog_form.html'
    success_url = reverse_lazy('home.html')


class BlogEntryDetailView(DetailView):
    model = BlogEntry
    template_name = 'blog_entry.html'
    context_object_name = 'blogentry'


class HomeListView(ListView):
    model = BlogEntry
    template_name = 'blog.html'
    context_object_name = 'blogentries'


class BlogDeleteView(DeleteView):
    model = BlogEntry
    template_name = 'blog_confirm.html'
    success_url = reverse_lazy('home.html')
