from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("api/v1/user", include("user.urls")),
    path("api/v1/news", include("news.urls")),
    path("api/v1/game", include("game.urls")),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
