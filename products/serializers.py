from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'pricce')