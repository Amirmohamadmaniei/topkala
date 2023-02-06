from django.urls import path, re_path
from . import views

app_name = 'product'

urlpatterns = [
    re_path(r'detail/(?P<pk>[-\w]+)/(?P<slug>[-\w]+)/', views.ProductDetailView.as_view(), name='detail'),
    re_path(r'list/category/(?P<category_slug>[-\w]+)/', views.ProductListCategoryView.as_view(), name='list_category'),
    re_path(r'list/sub-category/(?P<category_slug>[-\w]+)/(?P<sub_category_slug>[-\w]+)/', views.ProductListSubCategoryView.as_view(), name='list_sub_category'),
    re_path(r'list/subset/(?P<category_slug>[-\w]+)/(?P<sub_category_slug>[-\w]+)/(?P<subset_slug>[-\w]+)/', views.ProductListSubsetView.as_view(), name='list_subset'),
]
