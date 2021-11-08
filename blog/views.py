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

# Category view (functional view)
def CategoryView(request, cats):
    # Query "category" from the model and filter for the value of cats
    category_posts = Post.objects.filter(category=cats)
    
    # Context dictionary set to cats from urls.py file
    return render(
        request, 'categories.html', {
            'cats':cats, 
            'category_posts':category_posts,
        }
    )