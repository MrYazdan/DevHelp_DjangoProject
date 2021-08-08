from django.urls import path
from .views import *


urlpatterns = [
    path('login', login_user, name="login"),
    path('register', register, name="register"),
    path('logout', log_out, name="logout"),
    path('user', user_account_main_page, name="profile"),
    path('user/edit', edit_user_profile)
]
