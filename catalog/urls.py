from django.urls import path

from .views import (
    CategoryListAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    FeaturedProductListAPIView,
    NewArrivalProductListAPIView,
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),

    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/featured/', FeaturedProductListAPIView.as_view(), name='featured-products'),
    path('products/new-arrivals/', NewArrivalProductListAPIView.as_view(), name='new-arrival-products'),
    path('products/<slug:slug>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
