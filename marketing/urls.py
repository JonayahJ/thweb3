# Marketing URLs
from django.urls import path
from . import views

urlpatterns = [
    # Mailchimp marketing url
    path('', views.subscription, name="subscription"),
]