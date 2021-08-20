from django.urls import path

from order.views import *

urlpatterns = [
    path('', cart, name="cart"),
    path('add/', add_to_cart, name="add_to_cart"),
    path('final/', final, name="final-cart"),
]
