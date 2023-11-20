from django.shortcuts import render
from news.serializers import NewsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from game.models import Games

class GameListView(generics.ListAPIView):
    queryset = Games.objects.all().filter()
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_active', 'is_published', 'is_featured']