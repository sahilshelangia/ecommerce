from django.urls import path,re_path
from products.views import (
        ProductListView,
        # product_list_view,
        # ProductDetailView,
        # product_detail_view,
        # ProductFeaturedListView,
        # ProductFeaturedDetailView,
        ProductDetailSlugView,
    )

app_name='product'
urlpatterns = [
    path('',ProductListView.as_view(),name='list'),
    # path('featured/',ProductFeaturedListView.as_view(),name='ProductListView'),
    # path('products-fbv/',product_list_view,name='product_list_view'),
    # path('products/<pk>',ProductDetailView.as_view(),name='ProductDetailView'),
    re_path(r'^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(),name='detail'),

    # path('featured/<pk>',ProductFeaturedDetailView.as_view(),name='ProductDetailView'),
    # path('products-fbv/<pk>',product_detail_view,name='product_detail_view'),
]