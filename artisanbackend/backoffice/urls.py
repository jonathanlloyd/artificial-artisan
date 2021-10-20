"""URL config for backoffice"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
