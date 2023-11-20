from django.db import models
from rest_framework import serializers
from .models import Account, Customer

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        # fields = ['account_id', 'customer_id', 'account_number', 'balance']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        # fields = ['customer_id', 'name', 'email', 'phone_number']