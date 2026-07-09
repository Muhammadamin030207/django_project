from rest_framework import serializers

import subcategory
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    category=serializers.CharField(source='category.name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)


    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'category_name',
            'subcategory',
            'subcategory_name',
            'incoming_price',
            'stock',
            'created_at',
        ]
        read_only_fields = ['id', 'category_name', 'subcategory_name', 'created_at','created_date',]

    def create(self, validated_data):
        subcategory = validated_data.get("subcategory")

        if subcategory:
            validated_data["category"] = subcategory.category

            return Product.objects.create(**validated_data)



class UserProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'subcategory',
            'price',
            'stock',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']




