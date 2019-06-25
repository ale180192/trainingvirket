# import packages natives from python

# imports packages django
from django.contrib import admin

# owns packages
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


