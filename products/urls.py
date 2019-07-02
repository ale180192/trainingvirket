from rest_framework.urls import url
from django.urls import include

# owns packages
from .views import ProductList, ProductDetail
urlpatterns = [
    url(r'(?P<pk>[0-9]+)$', ProductDetail.as_view()),
    url(r'^$', ProductList.as_view()),
]



