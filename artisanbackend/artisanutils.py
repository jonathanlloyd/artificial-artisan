"""Utility functions shared amongst artisan apps"""

import os

from django.conf import settings
import toml


def get_user_config_path(filename):
    """Get the full path for a file in the user config directory"""
    return os.path.join(settings.USER_CONFIG_DIR, filename)


def get_manifest_file():
    """Load the parsed manifest file from user config (as a dict)"""
    with open(
        get_user_config_path('config.toml'),
        'r',
        encoding='utf-8',
    ) as manifest_file:
        manifest = toml.loads(manifest_file.read())
    return manifest


def get_user_template(template_name):
    """Load a template from the user config dir (as a string)"""
    try:
        filename = os.path.join('templates/', template_name)
        with open(
            get_user_config_path(filename),
            'r',
            encoding='utf-8',
        ) as template_file:
            template = template_file.read()
        return template
    except FileNotFoundError:
        return ""
