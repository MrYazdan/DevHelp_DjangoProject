from order.models import Order, OrderItem


def order_queryset(self):
    if self.request.user.is_superuser:
        return Order.objects.all()
    elif self.request.user.id:
        return Order.objects.filter(owner=self.request.user)


def orderitem_queryset(self):
    if self.request.user.is_superuser:
        return OrderItem.objects.all()
    elif self.request.user.id:
        return OrderItem.objects.filter(owner=self.request.user)