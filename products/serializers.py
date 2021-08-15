from rest_framework import serializers

from core.serializers import UserSerializer
from products.models import Product, Discount, OffCode
from category.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'


class OffCodeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = OffCode
        fields = '__all__'
