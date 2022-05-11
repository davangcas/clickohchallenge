import requests

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Product, Order, OrderDetail


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class OrderDetailSerializer(ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = '__all__'
    
    def create(self, validated_data):
        order_detail = OrderDetail.objects.create(**validated_data)
        order_detail.product.stock -= order_detail.quantity
        order_detail.product.save()
        order_detail.save()
        return order_detail


class OrderSerializer(ModelSerializer):

    details = OrderDetailSerializer(many=True, read_only=True)
    total = SerializerMethodField()
    total_usd = SerializerMethodField()


    class Meta:
        model = Order
        fields = ('date_time', 'details', 'total', 'total_usd')

    def get_total(self, instance):
        order_details = OrderDetail.objects.filter(order=instance)
        total = 0

        for order_detail in order_details:
            total += order_detail.product.price * order_detail.quantity

        return total

    def get_total_usd(self, instance):
        order_details = OrderDetail.objects.filter(order=instance)
        total = 0
        request = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')

        dolar_price = request.json()[1]['casa']['venta']

        for order_detail in order_details:
            total += order_detail.product.price * order_detail.quantity

        return float(total) * float(dolar_price.split(',')[0])
