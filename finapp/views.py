from django.shortcuts import render
from rest_framework import viewsets
from django.urls import include, re_path
from rest_framework_swagger.views import get_swagger_view

from .models import Account, Customer
from .serializers import AccountSerializer, CustomerSerializer

# Create your views here.
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    re_path(r'^$', schema_view)
]


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer