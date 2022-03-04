from .models import *
from rest_framework import serializers

from datetime import datetime


class PerevalSerializer(serializers.Serializer):
    pereval_id = serializers.IntegerField()
    beautyTitle = serializers.CharField()
    title = serializers.CharField()
    other_titles = serializers.CharField()
    connect = serializers.CharField(allow_blank=True)
    add_time = serializers.DateTimeField(allow_null=True)
    user = serializers.JSONField()
    coords = serializers.JSONField()
    type = serializers.CharField()
    level = serializers.JSONField()
    images = serializers.JSONField()

    def to_representation(self, instance):
        raw_data = instance.raw_data
        raw_data['images'] = instance.images
        return raw_data

    def create(self, validated_data):
        lst = ['beautyTitle', 'title', 'other_titles', 'connect', 'pereval_id', 'user', 'coords', 'type', 'level']
        raw_data = {}
        for name in lst:
            raw_data[name] = validated_data.pop(name)

        pereval = Pereval(date_added=validated_data.pop('add_time', datetime.now()), raw_data=raw_data,
                          images=validated_data.pop('images'))
        pereval.save()
        return pereval

    def update(self, instance, validated_data):
        lst = ['beautyTitle', 'title', 'other_titles', 'connect', 'pereval_id', 'coords', 'type', 'level']
        raw_data = {}
        for name in lst:
            raw_data[name] = validated_data.pop(name)

        instance.date_added = validated_data.pop('add_time', datetime.now())
        instance.raw_data = raw_data,
        instance.images = validated_data.pop('images')
        instance.save()
        return instance
