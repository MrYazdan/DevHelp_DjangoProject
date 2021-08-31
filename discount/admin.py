from django.contrib import admin
from .models import Discount, OffCode


@admin.register(Discount)
class DiscountModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active_to', 'percent', 'last_used']


@admin.register(OffCode)
class OffCodeModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active_to', 'code', 'limit', 'percent', 'last_used']
    filter_horizontal = ['for_users']