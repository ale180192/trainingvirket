# import packages natives from python

# imports packages django
from django.shortcuts import render
from django.contrib import admin
from rest_framework.views import APIView
from rest_framework.views import Response

# import packages owns
from .models import UserCustom




class UsersList(APIView):
    '''
        Manage users
    '''

    def get(self, request, format=None):
        '''
            List all users
        '''
        data = UserCustom.objects.all()

        return Response({'success': True, 'data': data, 'msg': 'ok'}, 200)

