from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("sites.api.v1.urls")),
    path('api/v1/signin/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh')
]


admin.site.site_header = "ROSKOMNADZOR"
admin.site.site_title = "ROSKOMNADZOR Admin Portal"
admin.site.index_title = "ROSKOMNADZOR Admin"

# swagger
schema_view = get_schema_view(
    openapi.Info(
        title="ROSKOMNADZOR API",
        default_version="v1",
        description="API documentation for ROSKOMNADZOR App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns += [
    path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
]

