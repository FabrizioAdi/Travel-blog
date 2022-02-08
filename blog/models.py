from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    options = (
        ('draft', 'Draft')
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    publish_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default='draft')