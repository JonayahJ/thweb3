# Main urls.py file
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # allows us to grab images uploaded from admin side
