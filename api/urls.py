from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('products/', ProductListView.as_view()),
    path('addresses/', AddressListView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('users/detail/<int:pk>', UserDetailView.as_view()),
    path('products/detail/<slug:url>', ProductDetailView.as_view()),
    path('addresses/detail/<int:pk>', AddressDetailView.as_view()),
    path('categories/detail/<slug:url>', CategoryDetailView.as_view()),
]
