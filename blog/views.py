from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Blog, BlogType


# Create your views here.

class BlogList(ListView):
    model = Blog
    ordering = '-create_time'
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_list'


class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'


class BlogTypeList(ListView):
    model = Blog
    ordering = '-create_time'
    template_name = 'blog/blog_type_list.html'
    context_object_name = 'blog_type_list'

    def get_queryset(self):
        self.blogtype = get_object_or_404(BlogType, pk=self.kwargs.get('pk'))
        queryset = self.blogtype.blogs.all().order_by('-create_time')# Blog.objects.filter(blog_type=blogtype)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogtype'] = self.blogtype
        return context
