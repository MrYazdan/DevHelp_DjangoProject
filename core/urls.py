from django.urls import path
from .views import partial_footer, partial_category, partial_offer, partial_search, partial_header, partial_nav

urlpatterns = [
    path('_landing/footer', partial_footer, name="partial_footer"),
    path('_landing/category', partial_category, name="partial_category"),
    path('_landing/offer', partial_offer, name="partial_offer"),
    path('_landing/search', partial_search, name="partial_search"),
    path('_landing/header', partial_header, name="partial_header"),
    path('_landing/header', partial_nav, name="partial_nav"),
]
