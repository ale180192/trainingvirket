from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.




class UserCustom(AbstractBaseUser):
    user = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = 'user'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']