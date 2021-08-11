from django.db import models
from core.models import BaseModel
from core.models import User
from category.models import Category
from django.utils.translation import gettext_lazy as _, get_language
from core.utils import *


class DiscountManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(active=True)

    def get_all(self):
        return super().get_queryset()


class Discount(models.Model):
    title_en = models.CharField(
        max_length=150, verbose_name=_("English title"), help_text=_("This is english name for discount item"))
    title_fa = models.CharField(
        max_length=150, verbose_name=_("Persian title"), help_text=_("This is persian name for discount item"))
    active_from = models.DateTimeField(auto_now_add=True, verbose_name=_("From datetime"),
                                       help_text=_("This is start discount datetime "))
    active_to = models.DateTimeField(verbose_name=_("Expire datetime"),
                                     help_text=_("This is expire discount datetime "))
    active = models.BooleanField(default=True, verbose_name=_("Is Active"), help_text=_("This is time "))
    count_use = models.PositiveIntegerField(default=1, verbose_name=_("Count of use"),
                                            help_text=_("This is count for use off code and expire"))
    last_used = models.DateTimeField(default=None, null=True, blank=True)
    max_price = models.PositiveIntegerField(verbose_name=_("Max Discount Price"), default=None, null=True, blank=True,
                                            help_text=_("This is max discount price item"))
    percent = models.PositiveIntegerField(verbose_name=_("Discount Percent"),
                                          help_text=_("This is discount percent"))

    objects = DiscountManager()

    @property
    def title(self):
        return self.title_en if get_language() == "en-US" else self.title_fa

    def deactive(self):
        self.active = False

    def final_discount(self, price: int):
        _max = self.max_price
        _discount = round((self.percent * price) / 100)
        return _max if _discount >= _max else _discount

    def __str__(self):
        return self.title


class OffCode(Discount):
    code = models.CharField(max_length=80, verbose_name=_("Code for discount"), default=str(uuid.uuid4()).split("-")[0],
                            help_text=_("This is unique code for discount"), unique=True)
    for_users = models.ManyToManyField(User, default=None, null=True, blank=True, verbose_name=_("For users"),
                                       help_text=_("this is off code availble for selected users"))
    # for_products = models.ManyToManyField(User, default=None, null=True, blank=True, verbose_name=_("For users"),
    #                                    help_text=_("this is off code availble for selected users"))
    # for_categories = models.ManyToManyField(User, default=None, null=True, blank=True, verbose_name=_("For users"),
    #                                    help_text=_("this is off code availble for selected users"))

    class Meta:
        verbose_name = _("OFFCode")
        verbose_name_plural = _("OFFCodes")

    def checker(self, user: User):
        return (user in self.for_users.all()) and self.active


class ExtraProductManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True)

    def get_product_by_id(self, product_id):
        return self.get_queryset().filter(id=product_id)

    def get_product_by_category_url(self, category_url):
        return self.get_queryset().filter(category__url=category_url)


class Product(BaseModel):
    title_en = models.CharField(
        max_length=150, verbose_name=_("English title"),
        help_text=_("This is english name of product item")
    )
    title_fa = models.CharField(
        max_length=150, verbose_name=_("Persian title"),
        help_text=_("This is persian name of product item")
    )
    short_description_en = models.CharField(
        max_length=400, verbose_name=_("English short description"),
        help_text=_("This is english short description of product item")
    )
    short_description_fa = models.CharField(
        max_length=400, verbose_name=_("Persian short description"),
        help_text=_("This is persian short description of product item")
    )
    description_en = models.TextField(
        verbose_name=_("English description"),
        help_text=_("This is english description of product item")
    )
    description_fa = models.TextField(
        verbose_name=_("Persian description"),
        help_text=_("This is persian description of product item")
    )
    price = models.PositiveIntegerField(verbose_name=_("Price item"), help_text=_("This is price item"))
    discount = models.ForeignKey(to=Discount, on_delete=models.SET_NULL, verbose_name=_("Discount"),
                                 help_text=_("This is discount for product item"), null=True, blank=True, default=None)
    image = models.ImageField(
        upload_to=Controllers.Image.img_renamer,
        verbose_name=_("Product Image"),
        help_text=_("This is image of product item")
    )
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE,
        verbose_name=_("Category of product"),
        help_text=_("This is category of product")
    )
    view_count = models.PositiveIntegerField(
        default=0, verbose_name=_("View counts"),
        help_text=_("This is count of view products")
    )
    is_offer = models.BooleanField(
        default=False, verbose_name=_("Offer"),
        help_text=_("This is status of offer product")
    )
    count_inventory = models.PositiveIntegerField(verbose_name=_("Count In Inventory"),
                                                  help_text=_("This is count of item in inventory"))
    count_buy = models.PositiveIntegerField(verbose_name=_("Count Of Buy"), default=0,
                                            help_text=_("This is count of buy item"))
    url = models.SlugField(verbose_name=_("Link"), default=Controllers.Product.url_creator, unique=True,
                           help_text=_("This is url or link name item -> /products/'url'"))

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    extra_objects = ExtraProductManager()

    @property
    def description(self):
        return self.description_en if get_language() == "en-US" else self.description_fa

    @property
    def short_description(self):
        return self.short_description_en if get_language() == "en-US" else self.short_description_fa

    @property
    def title(self):
        return self.title_en if get_language() == "en-US" else self.title_fa

    @property
    def final_price(self):
        return self.price - self.discount.final_discount(self.price) if self.discount else self.price

    @property
    def discount_count(self):
        return self.discount.final_discount(self.price) if self.discount else 0

    @property
    def product_url(self):
        return f"/products/{self.url}"

    def __str__(self):
        return self.title
