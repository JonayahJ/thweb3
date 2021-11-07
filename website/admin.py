from django.contrib import admin
from website.models import Member, Testimonial
from django.utils.html import  format_html

# Admin Table for Staff Members
class MemberAdmin(admin.ModelAdmin):
    # Allowing the headshot to show up in the admin table
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 15%" />'.format(object.headshot.url))

    # Setting the thumbnail name to Headshot
    thumbnail.short_description = 'Headshot'
    
    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'title')
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'title')
    list_filter = ('title',)
    ordering = ('id',)
    
# Staff Members
admin.site.register(Member, MemberAdmin)

# Admin Table for Testimonials
class TestimonialAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 15%" />'.format(object.headshot.url))
    
    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'name', 'num_of_stars')
    list_display_links = ('id', 'thumbnail', 'name')
    search_fields = ('name',)
    ordering = ('name',)

# Testimonials
admin.site.register(Testimonial, TestimonialAdmin)