from django.urls import path
from .views import CategoryProductShow, Categories

urlpatterns = [
    path('<slug:url>', CategoryProductShow.as_view(), name="category"),
    path('lists/', Categories.as_view(), name="categories"),
]