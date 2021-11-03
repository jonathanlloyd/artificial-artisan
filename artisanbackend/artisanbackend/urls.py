"""artisanbackend URL Configuration"""
from django.urls import include, path

urlpatterns = [
    path('artisan/', include('backoffice.urls')),
    path('', include('store.urls')),
]
