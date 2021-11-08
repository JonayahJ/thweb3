# Story admin
from django.contrib import admin
from .models import Story

# Stories
class StoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('organization',)}
    list_display = ('organization', 'industry', 'location')
    list_display_link = ('id', 'organization',)
    search_fields = ('organization',)
    list_filter = ('industry',)
    ordering = ('organization',)

admin.site.register(Story)