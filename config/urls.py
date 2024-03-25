from django.conf import settings
from django.contrib import admin
from django.urls import include, path

# API patterns for Admin
urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]

# API patterns for Local Apps
urlpatterns += [
    path(f"{settings.API_PREFIX}users/", include("apps.users.api.urls")),
]

# API patterns for Third Party Apps
urlpatterns += [
    path("accounts/", include("allauth.urls")),
]
