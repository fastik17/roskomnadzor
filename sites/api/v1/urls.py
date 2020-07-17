from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sites.api.v1.viewsets import RequestView, BlockedSitesView, RequestInfoView


router = DefaultRouter()
router.register('request', RequestView),
router.register('info', RequestInfoView),
router.register('blocked', BlockedSitesView),

urlpatterns = [
    path("", include(router.urls)),
]
