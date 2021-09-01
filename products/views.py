from itertools import product

from django.views.generic import ListView, DetailView

from account.models import Comment
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

    def get_context_data(self, **kwargs):
        kwargs["comments"] = Comment.objects.filter(product__id=self.object.id, is_accept=True)
        return super().get_context_data(**kwargs)


