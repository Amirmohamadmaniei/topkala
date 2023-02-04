from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>/<slug:slug>/', views.ProductDetail.as_view(), name='detail')
]
