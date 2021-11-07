# Story URLs
from django.urls import path
from .views import StoriesHomeView, StoryListView

urlpatterns = [
    path('', StoriesHomeView.as_view(), name="client-stories"),
    path('client-stories/<slug:slug>', StoryListView.as_view(), name="story-detail"),
]