from django.db import models

# Create your models here.
class Member(models.Model):

    headshot = models.ImageField(upload_to='photos/headshots', null=True, blank=True)
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25)
    middle_initial = models.CharField(max_length=1, null=True, blank=True)
    last_name = models.CharField(max_length=40)
    bio = models.TextField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True, default='https://www.linkedin.com/')
    github = models.URLField(null=True, blank=True, default='https://github.com/')

    def __str__(self):
        return self.first_name + ' ' + str(self.middle_initial)+'.' + ' ' + str(self.last_name)

class Testimonial(models.Model):
    headshot = models.ImageField(upload_to="photos/testimonials", null=True, blank=True)
    num_of_stars = models.FloatField(max_length=3)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    quote = models.TextField(max_length=300)

    def __str__(self):
        return self.name