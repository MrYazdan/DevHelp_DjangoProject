from django.urls import path
from .views import CategoryProductShow, Categories

urlpatterns = [
    path('<slug:url>', CategoryProductShow.as_view()),
    path('lists/', Categories.as_view(), name="categories"),
]