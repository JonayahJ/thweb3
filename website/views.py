from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import ListView
from website.models import Member, Testimonial


# Homepage
class IndexView(ListView):
    model = Testimonial
    template_name = 'index.html'

# About
class AboutView(ListView):
    model = Member
    template_name = 'about.html'

# Branding
def branding(request):
    return render(request, "branding.html", {})

# Client Stories
def client_stories(request):
    return render(request, "client-stories.html", {})

# Contact
def contact(request):
    return render(request, "contact.html", {})

# FAQ
def faq(request):
    return render(request, "faq.html", {})

# Hire Us
def hire_us(request):
    return render(request, "hire-us.html", {})

# Maintenance & Hosting
def maintenance_hosting(request):
    return render(request, "maintenance-hosting.html", {})

# Privacy
def privacy(request):
    return render(request, "privacy.html", {})

# Scheduler
def scheduler(request):
    return render(request, "scheduler.html", {})

# Terms
def terms(request):
    return render(request, "terms.html", {})

# Website Development
def website_development(request):
    return render(request, "website-development.html", {})