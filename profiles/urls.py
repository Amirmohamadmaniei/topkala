from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('personal/', views.ProfilePersonalView.as_view(), name='profile_personal'),
    path('edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('favorites/detail/', views.FavoriteDetailView.as_view(), name='favorites'),
    path('favorites/add/<int:product_id>/', views.FavoriteAddRemoveView.as_view(), name='add_favorite'),
    path('favorites/remove/<int:product_id>/', views.FavoriteRemoveView.as_view(), name='remove_favorite'),
]
