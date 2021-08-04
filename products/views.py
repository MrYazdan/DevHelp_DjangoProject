from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404
from category.models import Category
from .models import Product


class Products(ListView):
    template_name = "landing/products.html"
    paginate_by = 8

    def get_queryset(self):
        return Product.objects.get_active_list().filter(is_offer=False)

    def get_context_data(self, *args, object_list=None, **kwargs):
        kwargs["counter"] = Product.objects.count()
        return super().get_context_data(object_list=object_list, **kwargs)


class ProductDetail(DetailView):
    template_name = "landing/product_detail.html"
    model = Product
    slug_field = "url"