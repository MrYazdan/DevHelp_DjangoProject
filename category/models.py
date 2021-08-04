from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _, get_language
from core.utils import *


class Category(BaseModel):
    name_fa = models.CharField(
        max_length=150,
        verbose_name=_("Category FA Name"),
        help_text=_("This is persian name category item"),
        unique=True,
    )
    name_en = models.CharField(
        max_length=150,
        verbose_name=_("Category EN Name"),
        help_text=_("This is english name category item"),
        unique=True,
    )
    image = models.ImageField(
        upload_to=Controllers.Image.img_renamer, null=True, blank=True,
        verbose_name=_("Category image"),
        help_text=_("This is image of category item")
    )
    url = models.SlugField(unique=True, verbose_name=_("Link"),
                           help_text=_("This is url or link of category -> /category/'url'")
                           )
    description_en = models.TextField(
        default="This is test english category description", blank=True, null=True,
        verbose_name=_("English description"),
        help_text=_("This is english description for this category")
    )
    description_fa = models.TextField(
        default="این متن تست برای توضیحات بخش دسته بندی است", blank=True, null=True,
        verbose_name=_("Persian description"),
        help_text=_("This is persian description for this category")
    )

    @property
    def description(self):
        return self.description_en if get_language() == "en-US" else self.description_fa

    @property
    def name(self):
        return self.name_en if get_language() == "en-US" else self.name_fa

    def url_full(self):
        return f"/category/{self.url}"

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
