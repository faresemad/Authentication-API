from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# API patterns for Admin
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]

# API patterns for Local Apps
urlpatterns += [
    path(f"{settings.API_PREFIX}users/", include("apps.users.api.urls")),
]

# API patterns for Third Party Apps
urlpatterns += []

# API patterns for Spectacular
urlpatterns += [
    path(f"{settings.API_PREFIX}schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        f"{settings.API_PREFIX}docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]
