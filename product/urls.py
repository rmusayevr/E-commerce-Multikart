from django.urls import path
from .views import product_page, vendor_profile

urlpatterns = [
    path('product_page/', product_page, name='product_page'),
    path('vendor_profile/', vendor_profile, name='vendor_profile'),
]