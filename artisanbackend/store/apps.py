"""App config for store"""

from django.apps import AppConfig


class StoreConfig(AppConfig):
    """Top level object for store config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
