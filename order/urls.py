from django.urls import path

from order import views

app_name = 'order'

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='create'),
    path('detail/<int:order_id>/', views.OrderDetailView.as_view(), name='detail'),
    path('select-payment/<int:order_id>/', views.OrderSelectPayment.as_view(), name='select_payment'),
    # path('apply/<int:order_id>/', views.ApplyCouponView.as_view(), name='apply_coupon'),
]
