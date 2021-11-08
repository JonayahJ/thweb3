# Contact URLs
from django.urls import path
from . import views

urlpatterns = [
    path('inquiry', views.inquiry, name="inquiry"),
    path('req_quote', views.req_quote, name="req-quote"),
    path('thankyou', views.thankyou, name="thankyou"),
]