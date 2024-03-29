from rest_framework import serializers

from core.serializers import UserSerializer
from products.models import Product
from discount.models import Discount, OffCode
from category.serializers import CategorySerializer


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    product_url = serializers.CharField()
    short_description = serializers.CharField()
    description = serializers.CharField()
    category = CategorySerializer(read_only=True)
    discount = DiscountSerializer(read_only=True)
    final_discount = serializers.SerializerMethodField()

    def get_final_discount(self, obj):
        return obj.discount.final_discount(obj.price) if obj.discount else 0

    class Meta:
        model = Product
        fields = '__all__'


class OffCodeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    title = serializers.CharField()

    class Meta:
        model = OffCode
        fields = '__all__'
