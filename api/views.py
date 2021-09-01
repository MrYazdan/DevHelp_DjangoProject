from time import sleep
from rest_framework import status, response
from account.models import Comment
from account.serializers import CommentSerializer
from order.serializer import OrderSerializer, OrderItemSerializer
from settings.models import Contact
from settings.serializers import ContactSerializer
from products.models import Product, Category
from discount.models import Discount, OffCode
from products.serializers import ProductSerializer, DiscountSerializer, OffCodeSerializer, CategorySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, \
    UpdateAPIView, ListAPIView, CreateAPIView
from core.serializers import UserSerializer, AddressSerializer, ChangePasswordSerializer
from core.models import User, Address
from django.utils.translation import gettext_lazy as _, gettext as _g
from .utils import *
from api.permissions import *


# Account
class CommentListView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all() if self.request.user.is_superuser else Comment.objects.filter(is_accept=True)


class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        super().perform_update(serializer) if self.request.user.is_superuser else \
            response.Response({"error": _("Your access is forbidden!")}, status=status.HTTP_403_FORBIDDEN)

    def perform_destroy(self, instance):
        super().perform_destroy(instance) if self.request.user.is_superuser else \
            response.Response({"error": _("Your access is forbidden!")}, status=status.HTTP_403_FORBIDDEN)


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


# Core
class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAdminUser]


class UserDetailView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.all() if self.request.user.is_superuser else User.objects.filter(id=self.request.user.id)


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response({'success': _("Password updated successfully.")}, status=status.HTTP_200_OK)


class AddressListView(ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        super().perform_create(serializer)


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(owner=self.request.user)


# Order
class OrderListView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return order_queryset(self)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs) if self.get_queryset().first().payment_datetime else \
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

    def get_queryset(self):
        sleep(1)
        return super().get_queryset()


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
        return OffCode.objects.filter(for_users__username=self.request.user.username, active=True)

    def perform_destroy(self, instance):
        instance.deactive()
        super().perform_destroy(instance)


# Contact
class ContactCreateListView(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs) if self.request.user.is_superuser else \
            response.Response({_g("detail"): _g("Authentication credentials were not provided.")}, status=403)
