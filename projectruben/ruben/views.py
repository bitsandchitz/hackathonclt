from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Unit, Tenant
from .serializers import *


class unit_list(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class unit_detail(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class tenant_list(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class tenant_detail(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer

