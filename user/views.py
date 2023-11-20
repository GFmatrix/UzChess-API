from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from user.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from user.models import User


class UserListView(generics.ListAPIView):
    queryset = User.objects.all().filter()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = []
    search_fields = ['$email']
    serializer_class = UserSerializer
