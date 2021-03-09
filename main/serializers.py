from rest_framework import serializers
from .models import *


class ShortenerCreateSerializer(serializers.ModelSerializer):
    short = serializers.ReadOnlyField(source='short_url')

    class Meta:
        model = Shortener
        fields = ['long_url', 'short']


class ShortenerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['long_url', 'short_url', 'added']


class ShortenerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['long_url', 'short_url']