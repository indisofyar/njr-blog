from django.contrib import admin

from blog.models import BlogPage


# Register your models here.
@admin.register(BlogPage)
class BlogPageAdmin(admin.ModelAdmin):
    pass