from rest_framework.urls import url
from django.urls import include

# owns packages
from .views import ProductList
urlpatterns = [
    url(r'^$', ProductList.as_view()),
]



