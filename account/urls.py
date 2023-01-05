from django.urls import path
from .views import profile, forget_pwd, RegisterView, LoginView, activate
from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('profile/', profile, name='profile'),
    path('forget_password/', forget_pwd, name='forget_password'),
    # path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # path('password_reset_confirm/<str:uidb64>/<str:token>/',
        # CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('password_reset/password_reset_email_confirm/',
        # CustomResetEmailConfirmView.as_view(), name="password_reset_done"),
    # path('password_reset_confirm/password_reset_complete/',
        # CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),
]