from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True)


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(is_active=True).select_related('category')


class ProductDetailAPIView(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Product.objects.filter(is_active=True).select_related('category')


class FeaturedProductListAPIView(ProductListAPIView):
    def get_queryset(self):
        return super().get_queryset().filter(is_featured=True)


class NewArrivalProductListAPIView(ProductListAPIView):
    def get_queryset(self):
        return super().get_queryset().filter(is_new_arrival=True)
