from django.urls import path
from .views import error, about, contact, faq, home, search

urlpatterns = [ 
    path('error/', error, name='error'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('', home, name='home'),
    path('search/', search, name='search'),
]