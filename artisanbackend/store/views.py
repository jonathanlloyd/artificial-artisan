"""View methods for backoffice"""

from django.http import HttpResponse


def index(_):
    """Simple index view"""
    return HttpResponse('Store Homepage')
