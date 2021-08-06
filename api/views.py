from products.models import Product
from category.models import Category
from products.serializers import ProductSerializer
from category.serializers import CategorySerializer
from rest_framework.generics import GenericAPIView, mixins


class ProductListView(GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryListView(GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetailView(GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_url_kwarg = "url"
    lookup_field = "url"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        instance.is_deleted = True

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class CategoryDetailView(GenericAPIView, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_url_kwarg = "url"
    lookup_field = "url"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        instance.is_deleted = True

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
