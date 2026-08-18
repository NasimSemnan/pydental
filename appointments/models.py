from django.db import models
from django.utils import timezone


class Appointment(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    service = models.CharField(max_length=80)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.service}"


class BlogPost(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(max_length=80)
    excerpt = models.TextField()
    body = models.TextField()
    featured_image = models.URLField(max_length=500)
    author = models.CharField(max_length=120, default="Northstar Dental team")
    read_time = models.PositiveSmallIntegerField(default=4)
    published_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class PortfolioItem(models.Model):
    title = models.CharField(max_length=160)
    category = models.CharField(max_length=80)
    description = models.TextField()
    result = models.CharField(max_length=180)
    image_url = models.URLField(max_length=500)
    is_featured = models.BooleanField(default=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self):
        return self.title
