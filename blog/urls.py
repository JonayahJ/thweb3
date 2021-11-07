# Blog urls.py file
from django.urls import path
from .views import BlogHomeView, PostListView

urlpatterns = [
    path('', BlogHomeView.as_view(), name="blog"),
    path('post/<slug:slug>', PostListView.as_view(), name="post-detail"),
]
