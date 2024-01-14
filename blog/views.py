from catalog.views import UserIsVerified
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogForm, BlogUpdateForm
from blog.models import Blog

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class BlogCreateView(LoginRequiredMixin, UserIsVerified, CreateView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    form_class = BlogForm

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserIsVerified, UpdateView):
    model = Blog
    form_class = BlogUpdateForm
    # success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        # args=[self.kwargs.get('pk')] 'pk' we get from urls.py  "path('view/<int:pk>/'..." in any methods
        return reverse('blog:blog_view', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, UserIsVerified, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(LoginRequiredMixin, UserIsVerified, ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, UserIsVerified, DetailView):
    model = Blog

    # method to increase views count in blog_detail.html
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
