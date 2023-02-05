from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile-personal/', views.ProfilePersonalView.as_view(), name='profile_personal'),
    path('profile-edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('change-password/', views.ChangePassword.as_view(), name='change_password'),
]
