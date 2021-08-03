from django.shortcuts import render
from django.views.generic import ListView


class CategoryProductShow(ListView):
    template_name = "landing/products.html"
    paginate_by = 8

    pass