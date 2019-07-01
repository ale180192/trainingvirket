"""trainingvirke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

# third party
from rest_framework_simplejwt import views as jwt_views

# owns packages
from vkadmin.views import UsersList
from trainingvirke.settings import DEBUG


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    url(r'^vkadmin/', include('vkadmin.urls')),
    url(r'^products', include('products.urls'))
]


if DEBUG:
    import debug_toolbar

    urlpatterns += (
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )