from django.contrib import admin
from .models import SochialAccount, Site


@admin.register(SochialAccount)
class SochialAccountModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'gb_ico', 'is_active', 'is_deleted']
    list_editable = ['is_active']


@admin.register(Site)
class SiteModelAdmin(admin.ModelAdmin):
    list_display = ['full_title', 'url_full', 'short_description']
