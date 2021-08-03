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


class ProductsByCategory(ListView):
    template_name = "products_list.html"
    paginate_by = 8

    def get_queryset(self):
        print(self.kwargs)
        category_name = self.kwargs['category_name']
        category = get_object_or_404(Category.objects.filter(name_en__iexact=category_name))
        return Product.extra_objects.get_product_by_category(category_name)


class ProductDetail(DetailView):
    template_name = "landing/product_detail.html"
    model = Product
    slug_field = "url"
    # def get_queryset(self):
    #     return Product.objects.filter(
    #         id=self.kwargs['pid'],
    #     )