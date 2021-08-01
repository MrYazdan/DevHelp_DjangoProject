from django.contrib import admin
from .models import Product


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product_url', 'price', 'is_active', 'is_deleted']
    list_editable = ['is_active']

    class Meta:
        model = Product


admin.site.register(Product, ProductModelAdmin)