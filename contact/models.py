# Contact models
from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone = models.CharField(null=True, blank=True, max_length=20)
    message = models.TextField(blank=True, null=True)
    sent_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email