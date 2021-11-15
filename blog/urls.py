# Blog urls.py file
from django.urls import path
from .views import BlogHomeView, PostListView, CategoryView, AuthorProfileView

urlpatterns = [
    path('', BlogHomeView.as_view(), name="blog"),
    path('post/<slug:slug>', PostListView.as_view(), name='post-detail'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('profile/<int:id>', AuthorProfileView.as_view(), name="author-profile"),
    

]
