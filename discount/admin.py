from django.contrib import admin
from .models import OffCode


@admin.register(OffCode)
class OffCodeModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'code', 'percent', 'last_used', 'count_use', 'active_to', 'active']
