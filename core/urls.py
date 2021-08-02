from django.urls import path
from .views import partial_footer


urlpatterns = [
    path('_landing/footer', partial_footer, name="partial_footer")
]