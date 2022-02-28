from .models import *
from rest_framework import serializers


class PerevalSerializer(serializers.ModelSerializer):
    raw_data = serializers.JSONField()
    images = serializers.JSONField()

    class Meta:
        model = Pereval
        fields = ['raw_data', 'images']

    def create(self, validated_data):
        test = Pereval(raw_data=validated_data, images=validated_data['images'])
        test.save()
        return test
