from django.urls import path, include
from news.views import NewsListView

urlpatterns = [
    path("", NewsListView.as_view())
]
