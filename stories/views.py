# Story views
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from stories.models import Story

# Stories home view (main blog page)
class StoriesHomeView(ListView):
    model = Story
    template_name = 'story-list.html'
    # ordering = [-id] # order by reverse ID#

# Story view (individual articles)
class StoryListView(DetailView):
    model = Story
    template_name = 'story-detail.html'