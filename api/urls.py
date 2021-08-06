from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('products/detail/<slug:url>', ProductDetailView.as_view()),
    path('categories/detail/<slug:url>', CategoryDetailView.as_view()),
]