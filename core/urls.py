from django.urls import path
from .views import partial_footer, partial_category, partial_offer


urlpatterns = [
    path('_landing/footer', partial_footer, name="partial_footer"),
    path('_landing/category', partial_category, name="partial_category"),
    path('_landing/offer', partial_offer, name="partial_offer"),
]