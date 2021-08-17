from time import sleep
from rest_framework import status, response
from order.serializer import OrderSerializer, OrderItemSerializer
from products.models import Product, Discount, OffCode, Category
from products.serializers import ProductSerializer, DiscountSerializer, OffCodeSerializer, CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveUpdateAPIView
from core.serializers import UserSerializer, AddressSerializer
from core.models import User, Address
from django.utils.translation import gettext_lazy as _
from .utils import *
from api.permissions import *


# Category
class CategoryListView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AdminEditable]


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AdminEditable]
    lookup_url_kwarg = "url"
    lookup_field = "url"

    def perform_destroy(self, instance):
        instance.deleter()
        super().perform_destroy(instance)


# Contact


# Core
class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]


class UserDetailView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


# TODO : ADDRESS CHECKED!!!
class AddressListView(ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAdminUser]


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [permissions.IsAdminUser]


# Order

class OrderListView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return order_queryset(self)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs) if self.get_queryset().last().payment_datetime else \
            response.Response({"error": _("You have an unpaid order.")}, status=status.HTTP_406_NOT_ACCEPTABLE)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return order_queryset(self)

    def perform_destroy(self, instance):
        instance.deleter()
        super().perform_destroy(instance)


class OrderItemListView(ListCreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return orderitem_queryset(self)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs) if self.get_queryset().last().order.payment_datetime else \
            response.Response({"error": _("This order is closed.")}, status=status.HTTP_406_NOT_ACCEPTABLE)


class OrderItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        sleep(1)
        return orderitem_queryset(self)

    def perform_destroy(self, instance):
        instance.deleter()
        super().perform_destroy(instance)


# Products
class ProductListView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AdminEditable]


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = "url"
    lookup_field = "url"
    permission_classes = [AdminEditable]

    def perform_destroy(self, instance):
        instance.is_deleted = True
        super().perform_destroy(instance)


class DiscountListView(ListCreateAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
    permission_classes = [AdminEditable]


class DiscountDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
    permission_classes = [permissions.IsAdminUser]

    def perform_destroy(self, instance):
        instance.deactive()
        super().perform_destroy(instance)


class OffCodeListView(ListCreateAPIView):
    serializer_class = OffCodeSerializer
    queryset = OffCode.objects.all()
    permission_classes = [permissions.IsAdminUser]


class OffCodeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = OffCodeSerializer
    lookup_field = "code"
    lookup_url_kwarg = "code"
    permission_classes = [permissions.IsAuthenticated, AdminEditable]

    def get_queryset(self):
        offcodes = OffCode.objects.filter(for_users__username=self.request.user.username)
        return OffCode.objects.all() if self.request.user.is_superuser else offcodes

    def perform_destroy(self, instance):
        instance.deactive()
        super().perform_destroy(instance)