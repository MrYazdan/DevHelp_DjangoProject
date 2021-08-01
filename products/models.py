from django.db import models
from core.models import BaseModel , BaseManager
from category.models import Category
from django.utils.translation import gettext_lazy as _, get_language
from .utils import *


class ExtraProductManager(models.Manager):
    base = BaseManager()

    def get_product_by_id(self, product_id):
        return self.base.get_queryset().filter(id=product_id)

    def get_product_by_category(self, category_en_name):
        return self.base.get_queryset().filter(category__name_en__iexact=category_en_name)


class Product(BaseModel):
    title_en = models.CharField(
        max_length=150, verbose_name=_("English title"),
        help_text=_("This is english name of product item")
    )
    title_fa = models.CharField(
        max_length=150, verbose_name=_("Persian title"),
        help_text=_("This is persian name of product item")
    )
    description_en = models.TextField(
        verbose_name=_("English description"),
        help_text=_("This is english description of product item")
    )
    description_fa = models.TextField(
        verbose_name=_("Persian description"),
        help_text=_("This is persian description of product item")
    )
    price = models.IntegerField(verbose_name=_("Price item"), help_text=_("This is price item"))
    discount = models.IntegerField(verbose_name=_("Discount item"), help_text=_("This is discount of item"))
    image = models.ImageField(
        upload_to=Controllers.ProductItem.img_renamer, null=False, blank=False,
        verbose_name=_("Product Image"),
        help_text=_("This is image of product item")
    )
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE,
        verbose_name=_("Category of product"),
        help_text=_("This is category of product")
    )
    view_count = models.IntegerField(
        default=0, verbose_name=_("View counts"),
        help_text=_("This is count of view products")
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    extra_objects = ExtraProductManager()

    @property
    def description(self):
        return self.description_en if get_language() == "en-US" else self.description_fa

    @property
    def title(self):
        return self.title_en if get_language() == "en-US" else self.title_fa

    @property
    def final_price(self):
        return self.price - self.discount

    def get_product_url(self):
        return f"/products/{self.id}/{self.title_en.replace(' ', '-')}"

    def __str__(self):
        return self.title
