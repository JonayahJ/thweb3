# Website urls.py file
from django.urls import path
from . import views
from .views import AboutView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    # path('', views.subscription, name="subscription"),
    path('about.html', AboutView.as_view(), name="about"),
    path('branding.html', views.branding, name="branding"),
    path('contact.html', views.contact, name="contact"),
    path('faq.html', views.faq, name="faq"),
    path('maintenance-hosting.html', views.maintenance_hosting, name="maintenance_hosting"),
    path('privacy.html', views.privacy, name="privacy"),
    path('quote.html', views.quote, name="quote"),
    path('scheduler.html', views.scheduler, name="scheduler"),
    path('terms.html', views.terms, name="terms"),
    path('website-development.html', views.website_development, name="website_development"),
]