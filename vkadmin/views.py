# import packages natives from python

# imports packages django
from django.shortcuts import render
from django.contrib import admin

# third party packages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.authtoken.models import Token# import packages owns
from .models import User




class UsersList(APIView):
    '''
        Manage users
    '''
    authentications = (TokenAuthentication,)
    def get(self, request, format=None):
        '''
            List all users
        '''
        user = request.user
        print(user.id)
        print(user.email)
        data = User.objects.all().values()
        print('data: ', data)

        return Response({'success': True, 'data': data, 'msg': 'ok'}, status.HTTP_200_OK)

