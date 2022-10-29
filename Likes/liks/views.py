import json
from django.shortcuts import render
import requests
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import HttpResponse


class QuoteViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


class QuoteUserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = QuoteUserSerializer
    queryset = QuoteUser.objects.all()


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()


def custom(request):
    queryset = Quote.objects.all()
    data = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    param = request.GET.get('q', '')
    print(param)
    return HttpResponse(QuoteSerializer(queryset, many=True).data)