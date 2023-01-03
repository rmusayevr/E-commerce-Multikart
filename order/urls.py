from django.urls import path
from .views import cart, checkout, order_success, wishlist

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('order_success/', order_success, name='order_success'),
    path('wishlist/', wishlist, name='wishlist'),
]