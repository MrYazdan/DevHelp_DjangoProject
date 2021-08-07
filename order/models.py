from django.db import models
from core.models import User, BaseModel
from products.models import Product, OffCode
from django.utils.translation import gettext_lazy as _, get_language


class Status(BaseModel):
    state_en = models.CharField(verbose_name=_("English Order Status State"), max_length=90,
                                help_text=_("This is english order status state"))
    state_fa = models.CharField(verbose_name=_("Persian Order Status State"), max_length=90,
                                help_text=_("This is persian order status state"))
    description_en = models.TextField(
        verbose_name=_("English state description"),
        help_text=_("This is english description of product item"))
    description_fa = models.TextField(
        verbose_name=_("Persian state description"),
        help_text=_("This is persian description of product item"))

    class Meta:
        verbose_name = 'Order Status'
        verbose_name_plural = 'Order Statuses'

    @property
    def description(self):
        return self.description_en if get_language() == "en-US" else self.description_fa

    @property
    def state(self):
        return self.state_en if get_language() == "en-US" else self.state_fa


class Order(BaseModel):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_("Order Owner"),
                              help_text=_("This is owner for buy cart item"))
    status = models.ForeignKey(verbose_name=_("Status State"), to=Status, on_delete=models.CASCADE,
                               help_text=_("This is status for paid order"))
    offcode = models.ForeignKey(to=OffCode, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    payment_datetime = models.DateTimeField(blank=True, null=True, default=None, verbose_name=_("Payment Datetime"),
                                            help_text=_("This is payment datetime"))

    class Meta:
        verbose_name = 'Order Cart'
        verbose_name_plural = 'Order Carts'


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name=_("Order"),
                              help_text=_("This is order cart"))
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name=_("Product"),
                                help_text=_("This is product in cart"))
    price = models.PositiveIntegerField(verbose_name=_("Price"), help_text=_("This is price of this product"))
    count = models.PositiveIntegerField(verbose_name=_("Count"), help_text=_("This is count of this product"))

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'

    @property
    def get_full_price(self):
        return self.price * self.count
