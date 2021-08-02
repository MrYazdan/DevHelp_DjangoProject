from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product_url', 'price', 'is_offer', 'is_active', 'is_deleted']
    list_editable = ['is_offer']

# admin.site.register(Product, ProductModelAdmin)
