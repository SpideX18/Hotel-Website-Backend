from django.shortcuts import render
from .models import Room, Category
from .serializer import RoomSerializer, CategorySerializer
from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import api_view


class RoomView(viewsets.ModelViewSet):
    queryset = Room.objects.order_by('-id')
    serializer_class = RoomSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer