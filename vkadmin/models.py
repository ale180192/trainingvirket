from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from django.contrib.admin import AdminSite, site
from django.contrib import admin

# Create your models here.





class UserManager(BaseUserManager):

    def create_user(self, user, password, email, name):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(user=user,
                            email=email,
                            name=name)
        user.set_password(password)
        user.is_super = False
        user.is_staff = False
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, user, password, email, name):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(user=user,
                            email=email,
                            name=name)
        user.set_password(password)
        user.is_super = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

    
class User(AbstractBaseUser, PermissionsMixin):
    user = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    objects = UserManager()
    
    USERNAME_FIELD = 'user'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'email']

    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
)


class AdminModel(admin.ModelAdmin):

    def has_module_permission(self, request):
        return True