from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']
        read_only_fields = ['id']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'total_price', 'created_at', 'items']
        read_only_fields = ['id', 'total_price', 'created_at']


class OrderCreateSerializer(serializers.Serializer):
    def create(self, validated_data):
        user = self.context['request'].user
        card_items = user.cards.select_related('product').all()

        if not card_items.exists():
            raise serializers.ValidationError("Card is empty.")

        total = sum(item.quantity * item.product.price for item in card_items)
        order = Order.objects.create(user=user, total_price=total)

        order_items = [
            OrderItem(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )
            for item in card_items
        ]
        OrderItem.objects.bulk_create(order_items)
        card_items.delete()

        return order
