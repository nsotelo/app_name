from rest_framework import serializers
from {{ app_name }} import models


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.Model
