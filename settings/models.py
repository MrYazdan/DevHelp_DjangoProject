from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _, get_language


class SochialAccount(BaseModel):
    name_fa = models.CharField(
        max_length=50, verbose_name=_("Persian name"),
        help_text=_("This is persian name of sochial accounts")
    )
    name_en = models.CharField(
        max_length=50, verbose_name=_("English name"),
        help_text=_("This is english name of sochial accounts")
    )
    url = models.CharField(
        max_length=50, verbose_name=_("Link"),
        help_text=_("This is link of sochial accounts")
    )
    gb_ico = models.CharField(
        max_length=50, verbose_name=_("Icon"),
        help_text=_("This is icon of sochial accounts from gorbeh icon")
    )

    class Meta:
        verbose_name = _("SochialAccount")
        verbose_name_plural = _("SochialAccounts")

    @property
    def name(self):
        return self.name_en if get_language() == "en-US" else self.name_fa