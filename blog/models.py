from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog')

# Get categories from the model
categories = Category.objects.all().values_list('name', 'name')

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="admin") # If we delete the user, we delete all the posts by the user.
    authorHS = models.ImageField(upload_to="photos/blog/profile", null=True, blank=True) # 160x160
    author2 = models.CharField(max_length=100, null=True, blank=True)
    author2HS = models.ImageField(upload_to="photos/blog/profile", null=True, blank=True) # 160x160
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, choices=categories, default='coding')
    # tags =
    
    featured = models.BooleanField(null=True, default=False) # is featured post
    featDesc = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    featuredImage = models.ImageField(upload_to="photos/blog", null=True, blank=True) # 900x450
    cardTop = models.ImageField(upload_to="photos/blog", null=True, blank=True) # 500x280
    altDesc1 = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    excerpt = models.CharField(max_length=200, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.")

    body1 = models.TextField()
    # body1 = RichTextField(blank=True, null=True)
    bodyImage1 = models.ImageField(upload_to="photos/blog", null=True, blank=True) # 1920x800
    altDesc2 = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    body2 = models.TextField()
    # body2 = RichTextField(blank=True, null=True)
    
    quote = models.TextField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    
    body3 = models.TextField()
    # body3 = RichTextField(blank=True, null=True)
    bodyImage2 = models.ImageField(upload_to="photos/blog", null=True, blank=True) # 1920x800
    altDesc3 = models.CharField(max_length=100, null=True, blank=True, default="Lorem ipsum dolor sit amet")
    body4 = models.TextField()

    # Adding in the slugs for URLs and SEO
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Setting the slug to a keyword in the object (in this case, the title)
        return reverse('post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            # if not a slug, slugify the title of the object
            self.slug = slugify(self.title)
        # return the new slug on save (?)
        return super().save(*args, **kwargs)