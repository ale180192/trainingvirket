# import packages natives from python

# imports packages django
from django.contrib import admin

# owns packages
from .models import UserCustom

# Register your models here.

@admin.register(UserCustom)
class UserCustomAdmin(admin.ModelAdmin):
    pass


