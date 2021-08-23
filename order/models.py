import uuid
from jdatetime import datetime as dt
from django.db import models
from django_jalali.db import models as jmodels
from core.models import User, BaseModel, Address
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
        verbose_name = _('Order Status')
        verbose_name_plural = _('Order Statuses')

    @property
    def description(self):
        return self.description_en if get_language() == "en-US" else self.description_fa

    @property
    def state(self):
        return self.state_en if get_language() == "en-US" else self.state_fa

    def __str__(self):
        return self.state


class Order(BaseModel):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name=_("Order Owner"),
                              help_text=_("This is owner for buy cart item"))
    status = models.ForeignKey(verbose_name=_("Status State"), to=Status, on_delete=models.CASCADE,
                               help_text=_("This is status for paid order"))
    offcode = models.ForeignKey(to=OffCode, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    payment_datetime = jmodels.jDateTimeField(blank=True, null=True, default=None, verbose_name=_("Payment Datetime"),
                                              help_text=_("This is payment datetime"))
    address = models.ForeignKey(to=Address, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name=_("User address"), help_text=_("This is user address for your order"))
    recepie_id = models.CharField(max_length=64, verbose_name=_("Recepie ID"),
                                  help_text=_("This is recepie id for this order"), default="".join(
            list(filter(lambda x: x.isnumeric(), str(uuid.uuid4()).split("-")[0]))))

    class Meta:
        verbose_name = _('Order Cart')
        verbose_name_plural = _('Order Carts')

    @property
    def total_price(self):
        return sum([order_item.total_price for order_item in self.orderitem_set.all()])

    @property
    def total_discount(self) -> int:
        discount = sum([order_item.total_discount for order_item in self.orderitem_set.all()])
        return discount

    @property
    def total_offcode(self) -> int:
        check = self.offcode.checker(self.owner) if self.offcode else False
        off = self.offcode.final_discount(self.final_price) if check else 0
        return off

    @property
    def final_price(self):
        return sum([order_item.final_price for order_item in self.orderitem_set.all()])

    def paid(self):
        self.status = Status.objects.get(id=2)
        self.payment_datetime = dt.now()
        self.save()

    def __str__(self):
        return str(self.owner.username)


class OrderItem(BaseModel):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name=_("Order"),
                              help_text=_("This is order cart"))
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name=_("Product"),
                                help_text=_("This is product in cart"))
    price = models.PositiveIntegerField(verbose_name=_("Price"), help_text=_("This is price of this product"))
    count = models.PositiveIntegerField(verbose_name=_("Count"), help_text=_("This is count of this product"))

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')

    @property
    def total_price(self):
        return self.product.price * self.count

    @property
    def final_price(self):
        return self.product.final_price * self.count

    @property
    def total_discount(self):
        return self.product.discount_count * self.count

    def __str__(self):
        return f"item: {self.order.owner}"
