from rest_framework import serializers
from core.serializers import UserSerializer
from products.serializers import OffCodeSerializer, ProductSerializer
from .models import Status, Order, OrderItem


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(read_only=True)
    # status = StatusSerializer(read_only=True)
    # offcode = OffCodeSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'