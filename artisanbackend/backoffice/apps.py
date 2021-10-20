"""App config for backoffice"""

from django.apps import AppConfig


class BackofficeConfig(AppConfig):
    """Top level object for backoffice config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backoffice'
