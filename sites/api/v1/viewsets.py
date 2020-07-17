from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from sites.api.v1.serializers import UserRequestSerializer, \
    BlockedSitesSerializer, UserRequestInfoSerializer
from sites.models import UserRequest, BlockedSites


class RequestView(GenericViewSet, CreateModelMixin):
    """Requests to block some web-site from non-authenticated users"""
    serializer_class = UserRequestSerializer
    queryset = UserRequest.objects.all()
    permission_classes = [AllowAny]


class RequestInfoView(GenericViewSet, ListModelMixin):
    """Lists of websites for admin"""
    serializer_class = UserRequestInfoSerializer
    queryset = UserRequest.objects.all()
    permission_classes = [IsAuthenticated]


class BlockedSitesView(GenericViewSet, CreateModelMixin, ListModelMixin):
    """Admin decision to block or not"""
    serializer_class = BlockedSitesSerializer
    queryset = BlockedSites.objects.all()
    permission_classes = [IsAuthenticated]
