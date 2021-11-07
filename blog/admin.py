from django.contrib import admin
from .models import Post

# Post
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'post_date')
    search_fields = ('title', 'author')
    # list_filter = ('category',)
    ordering = ('post_date',)

admin.site.register(Post, PostAdmin)