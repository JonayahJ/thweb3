# Blog urls.py file
from django.urls import path
# from . import views
from .views import BlogHomeView, PostListView

urlpatterns = [
    # path('', views.blog, name="blog"),
    path('', BlogHomeView.as_view(), name="blog"),
    path('post/<slug:slug>', PostListView.as_view(), name="post-detail"),
]
