from django.urls import path, include
from user.views import UserListView

urlpatterns = [
    path("", UserListView.as_view())
]
