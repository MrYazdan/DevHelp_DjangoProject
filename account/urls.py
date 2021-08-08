from django.urls import path
from .views import *


urlpatterns = [
    path('login', login_user, name="login"),
    path('register', register, name="register"),
    path('logout', log_out, name="logout"),
    path('profile', profile, name="profile"),
    # path('profile/edit', profile_edit)
]
