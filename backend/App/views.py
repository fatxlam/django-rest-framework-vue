from django.shortcuts import render
from rest_framework import viewsets
from .models import AppMessage
from .serializers import AppMessageSerializers

class AppMessageViewSet(viewsets.ModelViewSet):
    queryset= AppMessage.objects.all().order_by('-create_date')
    serializers_class = AppMessageSerializers
