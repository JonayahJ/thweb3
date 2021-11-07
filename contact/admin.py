# Contact models
from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'sent_date')
    list_display_link = ('id', 'first_name',)
    search_fields = ('first_name', 'last_name', 'email', 'sent_date')

admin.site.register(Contact, ContactAdmin)