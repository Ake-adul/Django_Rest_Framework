from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'price', 'count', 'category', 'create_at')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'create_at')