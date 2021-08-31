from django.contrib import admin
from .models import MultiImages, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['image', 'default', 'is_active', 'is_deleted']
    list_editable = ['is_active']


class MultiImagesModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'is_deleted']
    list_editable = ['is_active']
    inlines = [ImageInline]


admin.site.register(MultiImages, MultiImagesModelAdmin)