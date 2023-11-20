from django.urls import path, include
from game.views import GameListView

urlpatterns = [
    path("", GameListView.as_view())
]
