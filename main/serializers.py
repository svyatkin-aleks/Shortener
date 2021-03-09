from rest_framework import serializers
from .models import *


class ShortenerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['long_url']


class ShortenerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['long_url', 'short_url', 'added']


class ShortenerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields = ['long_url', 'short_url']