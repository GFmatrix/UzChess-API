from django.shortcuts import render
from news.serializers import NewsSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from news.models import News

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all().filter()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['is_active', 'is_published', 'is_featured']
    search_fields = ['$title', '$description']