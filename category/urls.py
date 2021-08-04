from django.urls import path
from .views import CategoryProductShow

urlpatterns = [
    path('<slug:url>', CategoryProductShow.as_view())
]