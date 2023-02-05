from django.urls import path, re_path
from . import views

app_name = 'cart'

urlpatterns = [
    path('detail/', views.CartDetailView.as_view(), name='cart'),
    path('detail/empty/', views.CartDetailEmptyView.as_view(), name='cart_empty'),
    path('add/<int:pk>/', views.CartAdd.as_view(), name='add'),
    re_path(r'remove/(?P<unique_id>[-\w]+)/', views.CartRemove.as_view(), name='remove'),
]
