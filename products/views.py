from django.shortcuts import render

# third-party packages
from rest_framework.views import Response, View
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

# owns packages
from .serializers import ProductSerializer
from .models import Product

class ProductList(View):
    '''
        manage the products. We can create and list
    '''
    authentication = (TokenAuthentication,)
    def post(self, request, format=None):
        data = request.data
        product = ProductSerializer(data=data)
        if product.is_valid():
            product.save()
            return Response({'success': False, 'msg': product.errors, 'data': None}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'msg': product.errors, 'data': None}, status=status.HTTP_201_CREATED)
    def get(self, request, format=None):
        products = Product.objects.all().values()
        Response({'success': True, 'msg': 'ok list products', 'data': products})
