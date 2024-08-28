from django.urls import path, include
from .Login_urls import urlpatterns as Login_urls


urlpatterns = [
    path('/', include(Login_urls)),
]