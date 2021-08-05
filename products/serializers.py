from rest_framework import serializers
from products.models import Product
from category.models import Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='id')

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'image': {'read_only': True},
            'is_offer': {'read_only': True},
        }
