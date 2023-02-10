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
    path('forget-password/', views.ForgetPasswordView.as_view(), name='forget_password'),
    path('verify-phone/', views.VerifyPhoneView.as_view(), name='verify_phone'),
    path('set-password/', views.SetNewPasswordView.as_view(), name='set_password'),
]
