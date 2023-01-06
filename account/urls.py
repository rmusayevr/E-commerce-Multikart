from django.urls import path
from .views import (
                    RegisterView, 
                    LoginView, 
                    CustomPasswordResetView, 
                    CustomPasswordResetConfirmView, 
                    CustomPasswordChangeView,
                    profile, activate)
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('profile/', profile, name='profile'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/',
        CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('change_password/', CustomPasswordChangeView.as_view(), name = "change_password"),
]