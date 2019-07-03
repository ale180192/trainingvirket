from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist       
from django.forms.models import model_to_dict

# third-party packages
from rest_framework.views import Response, APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# owns packages
from .serializers import ProductSerializer
from .models import Product

class ProductList(APIView):
    '''
        manage the products. We can create and list
    '''
    authentication = (TokenAuthentication,)
    permissions = (IsAuthenticated,)
    def post(self, request, format=None):
        data = request.data
        product = ProductSerializer(data=data)
        if product.is_valid():
            product.save()
            return Response({'success': True, 'msg': 'ok :)', 'data': {'id': product.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({'success': False, 'msg': product.errors, 'data': None}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        products = Product.objects.all().values()
        return Response({'success': True, 'msg': 'ok list products', 'data': products}, status=status.HTTP_200_OK)



class ProductDetail(APIView):

    authentication = (TokenAuthentication,)
    permissions = (IsAuthenticated,)
    def get(self, request, pk, format=None):
        try:
            data = Product.objects.get(pk=pk)
            data_dict = ProductSerializer(data)
            return Response({'success': True, 'msg': 'ok', 'data': model_to_dict(data)}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response({'success': False, 'msg': 'Not found', 'data': None}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'success': False, 'msg': 'Error server', 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self, request, pk, format=None):
        data = request.data
        try:
            seri = ProductSerializer(data=data)
            if seri.is_valid():
                Product.objects.filter(pk=pk).update(**seri.data)
                return Response({'success': True, 'msg': 'update ok', 'data': None}, status=status.HTTP_200_OK)
            else:
                return Response({'success': True, 'msg': seri.errors, 'data': None}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'success': False, 'msg': 'Not found', 'data': None}, status=status.HTTP_404_NOT_FOUND)
        