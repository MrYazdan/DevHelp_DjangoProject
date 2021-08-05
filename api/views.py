from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from products.models import Product

from products.serializers import ProductSerializer


class ProductListView(APIView):

    def get(self, *args, format=None, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse({
            "products": serializer.data
        })

    @csrf_exempt
    def post(self, *args, format=None, **kwargs):
        serializer = ProductSerializer(data=self.request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status_code=400)
