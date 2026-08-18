from django.contrib import admin

from .models import Appointment, BlogPost, PortfolioItem


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "created_at")
    list_filter = ("service", "created_at")
    search_fields = ("name", "email", "message")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at", "is_published")
    list_filter = ("category", "is_published")
    search_fields = ("title", "excerpt", "body")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "result", "is_featured", "display_order")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "description", "result")
