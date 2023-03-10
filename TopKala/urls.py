from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('', include('account.urls', namespace='account')),
    path('product/', include('product.urls', namespace='product')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('profile/', include('profiles.urls', namespace='profile')),
    path('order/', include('order.urls', namespace='order')),
    path('comment/', include('comment.urls', namespace='comment')),
    path('payment/', include('payment.urls', namespace='payment')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
