from django.urls import path, re_path
from . import views

app_name = 'product'

urlpatterns = [
    re_path(r'detail/(?P<pk>[-\w]+)/(?P<slug>[-\w]+)/', views.ProductDetail.as_view(), name='detail'),
]
