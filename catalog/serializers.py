from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
            'description',
            'image',
            'product_count',
        ]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    discount_percent = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'slug',
            'description',
            'price',
            'old_price',
            'image',
            'stock',
            'is_featured',
            'is_new_arrival',
            'discount_percent',
            'created_at',
        ]
