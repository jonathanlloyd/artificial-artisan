"""artisanbackend URL Configuration"""
from django.urls import include, path, re_path

urlpatterns = [
    path('backoffice/', include('backoffice.urls')),
    path('', include('store.urls')),
    re_path(r'^.*/$', include('store.urls')),
]
