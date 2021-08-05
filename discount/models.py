from django.db import models
from django.utils import timezone as tz
from category.models import Category
from products.models import Product
from core.models import User
from django.utils.translation import gettext_lazy as _, get_language


class BaseDiscountManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(active=True)

    def get_all(self):
        return super().get_queryset()


class BaseDiscountModel(models.Model):
    title_en = models.CharField(
        max_length=150, verbose_name=_("English title"),
        help_text=_("This is english name for discount item")
    )
    title_fa = models.CharField(
        max_length=150, verbose_name=_("Persian title"),
        help_text=_("This is persian name for discount item")
    )
    active_from = models.DateTimeField(auto_now_add=True, verbose_name=_("From datetime"),
                                       help_text=_("This is start discount datetime "))
    active_to = models.DateTimeField(auto_now_add=True, verbose_name=_("Expire datetime"),
                                     help_text=_("This is expire discount datetime "))
    active = models.BooleanField(default=True, verbose_name=_("Is Active"), help_text=_("This is time "))
    count_use = models.PositiveIntegerField(default=1, verbose_name=_("Count of use"),
                                            help_text=_("This is count for use off code and expire"))
    last_used = models.DateTimeField(default=None, null=True, blank=True, hidden=True)

    objects = BaseDiscountManager()

    @property
    def title(self):
        return self.title_en if get_language() == "en-US" else self.title_fa

    def deactive(self):
        self.active = False

    def check(self):
        if (not self.count_use) or (self.active_from < tz.now()):
            self.deactive()

    def use(self):
        self.count_use -= 1
        self.last_used = tz.now()
        self.check()

    def __str__(self):
        return self.title


class OffCode(BaseDiscountModel):
    code = models.CharField(min_length=3, max_length=80, verbose_name=_("Code for discount"),
                            help_text=_("This is unique code for discount"), unique=True)
    percent = models.PositiveIntegerField(max_length=2, verbose_name=_("Percent of off"),
                                          help_text=_("This is discount percent"))
    for_users = models.ManyToManyField(to=User, default=None, null=True, blank=True, verbose_name=_("For users"),
                                       help_text=_("this is off code availble for selected users")
                                       )
    for_products = models.ManyToManyField(to=Product, default=None, null=True, blank=True,
                                          verbose_name=_("For products"),
                                          help_text=_("this is off code availble for selected products")
                                          )
    for_category = models.ManyToManyField(to=Category, default=None, null=True, blank=True,
                                          verbose_name=_("For category"),
                                          help_text=_("this is off code availble for selected category")
                                          )

    class Meta:
        verbose_name = _("OFFCode")
        verbose_plural = _("OFFCodes")
