# import packages natives from python

# imports packages django
from django.shortcuts import render
from django.contrib import admin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# import packages owns
from .models import UserCustom




class UsersList(APIView):
    '''
        Manage users
    '''
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        '''
            List all users
        '''
        data = UserCustom.objects.all().values()

        return Response({'success': True, 'data': data, 'msg': 'ok'}, status.HTTP_200_OK)

