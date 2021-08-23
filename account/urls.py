from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('login', login_user, name="login"),
    path('register', register, name="register"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('profile', Profile.as_view(), name="profile"),
    path('profile/address', AddressView.as_view(), name="address"),
    path('profile/paid', UserOrders.as_view(), name="user_orders"),
    path('profile/offcode', AddressView.as_view(), name="user_offcode"),
    path('forget_password', forget_password, name="forget_password"),
]
