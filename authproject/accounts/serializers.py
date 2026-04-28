from rest_framework import serializers
from .models import Product, CartItem, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image']

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'quantity', 'subtotal']

    def get_subtotal(self, obj):
        return obj.product.price * obj.quantity


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['product_name', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = ['id', 'total_amount', 'status', 'address', 'phone', 'created_at', 'items']