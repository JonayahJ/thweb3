from django.contrib import admin
from .models import Category, Post

# Post
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'post_date')
    search_fields = ('title', 'author')
    list_filter = ('category',)
    ordering = ('post_date',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
