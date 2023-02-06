from django.urls import path

from order import views

app_name = 'order'

urlpatterns = [
    path('information/', views.OrderInformationView.as_view(), name='information')
]