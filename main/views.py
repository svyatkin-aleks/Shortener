from django.shortcuts import redirect
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, GenericAPIView
)
from .serializers import *
from .models import Shortener


class ShortenerCreateView(CreateAPIView):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerCreateSerializer


class ShortenerListView(ListAPIView):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerListSerializer


class ShortenerRetrievView(RetrieveAPIView):
    queryset = Shortener.objects.all()
    serializer_class = ShortenerRetrieveSerializer
    lookup_field = 'long_url'


def urlRedirect(request, short_url):
    data = Shortener.objects.get(short_url=short_url)
    return redirect(data.long_url)
