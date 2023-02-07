from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('confirm/', views.ConfirmOTPView.as_view(), name='confirm'),
    path('send-otp/', views.SendOTP.as_view(), name='send_otp'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('change-password/', views.ChangePassword.as_view(), name='change_password'),
]
