from django.views.generic import ListView
from category.models import Category
from products.models import Product


class CategoryProductShow(ListView):
    template_name = "landing/products_no_offer.html"
    paginate_by = 8

    def get_queryset(self):
        category_url = self.kwargs['url']
        return Product.extra_objects.get_product_by_category_url(category_url)

    def get_context_data(self, *args, object_list=None, **kwargs):
        kwargs["category"] = Category.objects.filter(url=self.kwargs["url"]).first()
        return super().get_context_data(object_list=object_list, **kwargs)


class Categories(ListView):
    template_name = "landing/categories.html"
    queryset = Category.objects.get_active_list()
    paginate_by = 4
