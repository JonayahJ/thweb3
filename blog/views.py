# Blog views
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post

# Blog home view (main blog page)
class BlogHomeView(ListView):
    model = Post
    template_name = 'blog.html'
    # ordering = [-id] # order by reverse ID#

# Post view (individual articles)
class PostListView(DetailView):
    model = Post
    template_name = 'post.html'