from django.urls import path
from .views import *


app_name = "main"

urlpatterns = [
    path('shortener/create', ShortenerCreateView.as_view()),
    path('shortener/list', ShortenerListView.as_view()),
    path('shortener/<path:long_url>', ShortenerRetrievView.as_view()),
    path('<str:short_url>', urlRedirect, name='urlRedirect')
]

