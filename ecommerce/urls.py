from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, OrderViewSet, OrderDetailViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'order-details', OrderDetailViewSet, basename='order_detail')

urlpatterns = router.urls
