# Stories model
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=255, default='Story title')
    organization = models.CharField(max_length=255, default='Orgnization Name')

    # Card details
    cardTop = models.ImageField(upload_to="photos/stories", null=True, blank=True) # 480x320/
    altDesc1 = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    excerpt = models.TextField(max_length=200, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.")

    # Metadata
    logo = models.ImageField(upload_to="logos", null=True, blank=True) # 356x110
    industry = models.CharField(max_length=50, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    location = models.CharField(max_length=50, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    goals = models.CharField(max_length=200, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    type_of_business = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    service1 = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    service2 = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")

    # Links
    website = models.URLField(null=True, blank=True, default='https://thinkhalcyon.com/')
    github = models.URLField(null=True, blank=True, default='https://github.com/')

    # Body
    body1 = models.TextField()
    bodyImage1 = models.ImageField(upload_to="photos/stories", null=True, blank=True) # 1920x800
    altDesc2 = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    body2 = models.TextField()
    bodyImage2 = models.ImageField(upload_to="photos/stories", null=True, blank=True) # 1920x800
    altDesc3 = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    body3 = models.TextField()

    # Quote
    quote = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)

    # Adding in the slugs for URLs and SEO
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name_plural = 'Stories'


    def __str__(self):
        return self.organization

    def get_absolute_url(self):
        # Setting the slug to a keyword in the object (in this case, the organization)
        return reverse('story-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # if not a slug, slugify the organization of the object
            self.slug = slugify(self.organization)
        # return the new slug on save (?)
        return super().save(*args, **kwargs)