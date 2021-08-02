from django.contrib import admin
from .models import SochialAccount


@admin.register(SochialAccount)
class SochialAccountModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'gb_ico', 'is_active', 'is_deleted']
    list_editable = ['gb_ico']
