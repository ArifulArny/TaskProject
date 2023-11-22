from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ShopViewSet, ProductCategoryViewSet, ProductColorViewSet, ProductViewSet, CartItemViewSet, OrderViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')
router.register(r'shops', ShopViewSet, basename='shops')
router.register(r'product-categories', ProductCategoryViewSet, basename='product-categories')
router.register(r'product-colors', ProductColorViewSet, basename='product-colors')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'cart-items', CartItemViewSet, basename='cart-items')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
]
