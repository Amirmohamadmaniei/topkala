from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('request/<int:order_id>/', views.SendRequestView.as_view(), name='request'),
    path('verify/', views.VerifyView.as_view(), name='verify'),
]
