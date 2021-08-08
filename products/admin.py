from django.contrib import admin
from .models import Product, Discount, OffCode


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product_url', 'price', 'is_offer', 'is_active', 'is_deleted']
    list_editable = ['is_offer']


@admin.register(Discount)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active_to', 'count_use', 'percent', 'last_used', 'active']


@admin.register(OffCode)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active_to', 'code', 'count_use', 'percent', 'last_used', 'active']
