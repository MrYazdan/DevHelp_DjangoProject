from django.urls import path
from .views import CategoryProductShow

urlpatterns = [
    path('<slug:slug>', CategoryProductShow)
]