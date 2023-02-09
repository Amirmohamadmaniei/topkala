from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('amazing/', views.AmazingView.as_view(), name='amazing'),
    path('serach/', views.SearchListView.as_view(), name='search'),
]
