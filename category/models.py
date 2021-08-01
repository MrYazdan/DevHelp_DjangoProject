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

    @property
    def name(self):
        return self.name_en if get_language() == "en-US" else self.name_fa

    @property
    def url_name(self):
        return self.name_en if " " not in self.name_en else self.name_en.replace(" ", "_")

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
