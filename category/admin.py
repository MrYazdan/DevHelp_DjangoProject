from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'is_active', 'is_deleted']
