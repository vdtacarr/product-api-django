from rest_framework import serializers
from .models import *
from django.contrib.auth.models import  User


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        exclude = ('id',)

class QuoteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteUser
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)