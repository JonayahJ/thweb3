# Marketing views
from django.shortcuts import render
from django.contrib import messages


# Mailchimp Marketing
def subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        print(email)
        messages.success(request, "Thank you for subscribing!") # message
    return render(request, 'marketing/index.html')