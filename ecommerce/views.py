from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Product, Order, OrderDetail
from .serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailViewSet(ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetail.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data.get('product')
            quantity = int(serializer.validated_data.get('quantity'))
            order_details = OrderDetail.objects.filter(order=serializer.validated_data.get('order'))

            if not product:
                return Response({
                    'error': 'Product not found',
                })

            if order_details.filter(product=product):
                return Response({
                    'error': 'Product already parsed in current order',
                })

            if product.stock < quantity:
                return Response({
                    'error': 'Without stock of the product selected',
                })

            serializer.save()

            return Response({
                'message': 'Order Detail Created',
            })
        return Response({'error': serializer.errors})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.product.stock += instance.quantity
        instance.product.save()
        self.perform_destroy(instance)

        return Response(data={
            'message': 'Order Detail Deleted',
        }, status=status.HTTP_204_NO_CONTENT)
