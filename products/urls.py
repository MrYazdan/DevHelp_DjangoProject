from django.urls import path
from .views import ProductDetail, Products


urlpatterns = [
    path('', Products.as_view(), name="products"),
    path('<slug:slug>', ProductDetail.as_view()),
]