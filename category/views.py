from django.views.generic import ListView
from category.models import Category
from products.models import Product


class CategoryProductShow(ListView):
    template_name = "landing/products_no_offer.html"
    paginate_by = 8

    def get_queryset(self):
        category_url = self.kwargs['url']
        return Product.objects.filter(category__url=category_url)

    def get_context_data(self, *args, object_list=None, **kwargs):
        kwargs["category"] = Category.objects.filter(url=self.kwargs["url"]).first()
        return super().get_context_data(object_list=object_list, **kwargs)


class Categories(ListView):
    template_name = "landing/categories.html"
    queryset = Category.objects.all()
    paginate_by = 4
