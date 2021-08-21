from django.urls import path
from django.views.generic import TemplateView

from .views import contact

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="landing/about.html"), name="about"),
    path('contact/', contact, name="contact"),
]