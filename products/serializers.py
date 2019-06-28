from rest_framework.serializers import Serializer
from rest_framework import serializers

from .models import Product


class ProductSerializer(Serializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'pricce')