import uuid
from django.db import models
from django.utils.translation import get_language, gettext_lazy as _
from core.models import LogicalModel, TimeStampMixin, User
from django_jalali.db import models as jmodels
from jdatetime import datetime as dt


class DiscountManager(models.Manager):

    def get_all(self):
        return super().get_queryset()


class BaseDiscountModel(LogicalModel, TimeStampMixin):
    title_en = models.CharField(max_length=150, verbose_name=_("English title"),
                                help_text=_("This is english name for discount item"))
    title_fa = models.CharField(max_length=150, verbose_name=_("Persian title"),
                                help_text=_("This is persian name for discount item"))
    active_from = jmodels.jDateTimeField(auto_now_add=True, verbose_name=_("From datetime"),
                                         help_text=_("This is start discount datetime "))
    active_to = jmodels.jDateTimeField(verbose_name=_("Expire datetime"),
                                       help_text=_("This is expire discount datetime "))
    last_used = jmodels.jDateTimeField(default=None, null=True, blank=True, verbose_name=_("Last Discount Used"),
                                       help_text=_("This is last used of discount"))
    max_price = models.PositiveIntegerField(verbose_name=_("Max Discount Price"), default=None, null=True, blank=True,
                                            help_text=_("This is max discount price item"))
    percent = models.PositiveIntegerField(verbose_name=_("Discount Percent"),
                                          help_text=_("This is discount percent"))

    class Meta:
        abstract = True

    @property
    def title(self):
        return self.title_en if get_language() == "en-US" else self.title_fa

    def final_discount(self, price: int) -> int:
        _max = self.max_price
        _discount = round((self.percent * price) / 100)
        return _max if _discount >= _max else _discount

    def expire_checker(self) -> bool:
        now = dt.now()
        if self.active_from <= now < self.active_to:
            return True
        self.deactive()
        return False

    extra_objects = DiscountManager()


class Discount(BaseDiscountModel):
    class Meta:
        verbose_name = _("Discount")
        verbose_name_plural = _("Discounts")

    def __str__(self):
        return self.title


class OffCode(BaseDiscountModel):
    code = models.CharField(max_length=80, verbose_name=_("Code for discount"), default=str(uuid.uuid4()).split("-")[0],
                            help_text=_("This is unique code for discount"), unique=True)
    for_users = models.ManyToManyField(User, default=None, null=True, blank=True, verbose_name=_("For users"),
                                       help_text=_("this is off code availble for selected users"))

    class Meta:
        verbose_name = _("OFFCode")
        verbose_name_plural = _("OFFCodes")

    def checker(self, user: User):
        return (user in self.for_users.all()) and self.is_active
