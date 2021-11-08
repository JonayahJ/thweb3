# Contact models
from django.db import models
from datetime import datetime

# Contact
class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone = models.CharField(null=True, blank=True, max_length=20)
    message = models.TextField(blank=True, null=True)
    sent_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email

# Quote
budget_options = [('$0-1k','$0-1,000'), ('$1k-2k','$1,000-2,000'), ('$2k-5k','$2,000-5,000'), ('$5k-10k','$5000-10,000'), ('$10k+','$10k+')]

class Quote(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    company = models.CharField(null=True, blank=True, max_length=50)
    budget = models.CharField(choices=budget_options, max_length=50)
    message = models.TextField(blank=True, null=True)
    sent_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email