from .models import *
from rest_framework import serializers


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdded
        fields = ['raw_data', 'images']

    def create(self, validated_data):
        pereval = PerevalAdded.objects.update_or_create(**validated_data)
        print("create pereval")
        return pereval
