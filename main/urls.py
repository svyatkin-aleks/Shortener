from django.urls import path
from .views import *


app_name = "main"

urlpatterns = [
    path('shortener/create', ShortenerCreateView.as_view()),
    path('shortener/list', ShortenerListView.as_view()),
    path('shortener/short/<str:short_url>', ShortenerRetrievView.as_view()),
    path('redirect/<str:short_url>', urlRedirect, name='urlRedirect')
]

