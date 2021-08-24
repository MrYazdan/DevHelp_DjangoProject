from django.urls import path
from .views import *

app_name = "api"
urlpatterns = [
    # Category
    path('categories/', CategoryListView.as_view()),
    path('categories/detail/<slug:url>', CategoryDetailView.as_view()),
    # Core
    path('users/', UserListView.as_view()),
    path('users/detail/<int:pk>', UserDetailView.as_view(), name="user_detail"),
    path('users/passwords/update/<int:pk>', ChangePasswordView.as_view(), name="change_password"),
    path('addresses/', AddressListView.as_view(), name="address"),
    path('addresses/detail/<int:pk>', AddressDetailView.as_view()),
    # Order
    path('orders/', OrderListView.as_view(), name="orders"),
    path('orders/detail/<int:pk>', OrderDetailView.as_view()),
    path('orderitems/', OrderItemListView.as_view(), name="orderitems"),
    path('orderitems/detail/<int:pk>', OrderItemDetailView.as_view(), name="orderitems_detail"),
    # Products
    path('products/', ProductListView.as_view(), name="products"),
    path('products/detail/<slug:url>', ProductDetailView.as_view()),
    path('discounts/', DiscountListView.as_view()),
    path('discounts/detail/<int:pk>', DiscountDetailView.as_view()),
    path('offcodes/', OffCodeListView.as_view()),
    path('offcodes/detail/<str:code>', OffCodeDetailView.as_view(), name="offcode_detail"),
    # Contact
    path('contacts/', ContactCreateListView.as_view(), name="contact"),
]
