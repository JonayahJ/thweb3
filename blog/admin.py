from django.contrib import admin
from .models import Category, Post, Profile
from django.utils.html import  format_html

# Post
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'post_date')
    search_fields = ('title', 'author')
    list_filter = ('category',)
    ordering = ('post_date',)

# Profile
class ProfileAdmin(admin.ModelAdmin):
    # Allowing the headshot to show up in the admin table
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 15%" />'.format(object.headshot.url))
    
    # Setting the thumbnail name to Headshot
    thumbnail.short_description = 'Headshot'

    list_display = ('thumbnail', 'user')
    list_display_links = ('thumbnail', 'user')
    search_fields = ('user',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Profile, ProfileAdmin)
