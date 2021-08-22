from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="landing/about.html"), name="about"),
    path('contact/', TemplateView.as_view(template_name="landing/contact.html"), name="contact"),
]