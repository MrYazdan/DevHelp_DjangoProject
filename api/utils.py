from order.models import Order, OrderItem


def order_queryset(self):
    return Order.objects.all() if self.request.user.is_superuser else Order.objects.filter(owner=self.request.user)


def orderitem_queryset(self):
    return OrderItem.objects.all() if self.request.user.is_superuser else OrderItem.objects.filter(
        order__owner=self.request.user)
