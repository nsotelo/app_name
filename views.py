from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from {{ app_name }} import models
from {{ app_name }} import permissions as custom_permissions
from {{ app_name }} import serializers


class CRUDViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update`
    and destroy actions.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.Model.objects.all()
    serializer_class = serializers.ModelSerializer


class OwnedViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.Permission,
    ]
    queryset = Session.objects.all()
    serializer_class = serializers.ModelSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ROViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """

    queryset = models.Model.objects.all()
    serializer_class = ModelSerializer
