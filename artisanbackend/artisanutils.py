"""Utility functions shared amongst artisan apps"""

import os

from django.conf import settings
import toml


def get_user_config_path(filename):
    return os.path.join(settings.USER_CONFIG_DIR, filename)


with open(get_user_config_path('config.toml'), 'r') as f:
    MANIFEST_FILE = toml.loads(f.read())


def get_user_template(template_name):
    filename = os.path.join('templates/', template_name)
    with open(get_user_config_path(filename), 'r') as f:
        template = f.read()
    return template
