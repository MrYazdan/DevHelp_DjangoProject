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
