from django.urls import path
from .views import *


urlpatterns = [
    path('login', login_user, name="login"),
    path('register', register, name="register"),
    path('logout', log_out, name="logout"),
    path('profile', profile, name="profile"),
    path('forget_password', forget_password, name="forget_password"),
]
