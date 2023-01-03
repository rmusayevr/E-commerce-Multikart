from django.urls import path
from .views import login, register, profile, forget_pwd

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('forget_password/', forget_pwd, name='forget_password'),
]