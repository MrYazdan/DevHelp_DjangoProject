from rest_framework import status, response
from order.models import Order, OrderItem
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
class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [AdminEditable]
    lookup_url_kwarg = "url"
    lookup_field = "url"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        instance.is_deleted = True


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
            response.Response({"detail": _("You have an unpaid order.")}, status=status.HTTP_406_NOT_ACCEPTABLE)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return orderitem_queryset(self)


class OrderItemListView(ListCreateAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return user_queryset(self, OrderItem)


class OrderItemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return user_queryset(self, OrderItem)


# Products
class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = "url"
    lookup_field = "url"
    permission_classes = [AdminEditable]

    def perform_destroy(self, instance):
        instance.is_deleted = True


class DiscountListView(ListAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
    permission_classes = [AdminEditable]


class DiscountDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
    permission_classes = [permissions.IsAdminUser]


class OffCodeListView(ListAPIView):
    serializer_class = OffCodeSerializer
    queryset = OffCode.objects.all()
    permission_classes = [permissions.IsAdminUser]


class OffCodeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = OffCodeSerializer
    queryset = OffCode.objects.all()
    permission_classes = [permissions.IsAdminUser]
