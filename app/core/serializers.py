from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer для модели заказа
    """
    class Meta:
        model = Order
        fields = ('number', 'order_number', 'cost_in_usd', 'cost_in_rub', 'delivery_date')
