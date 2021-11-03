"""Tests for store"""

from contextlib import contextmanager
import importlib
import os
import tempfile

from django.test import Client, TestCase
import toml

from store import views as store_views


class TestLandingPage(TestCase):
    """Test that the landing page is correctly rendered"""

    def test_golden_path(self):
        """Test basic landing page rendering"""
        # Given user config with correct templates
        title = 'BlueIce Art'
        global_head_template = '''
            <link rel="stylesheet" href="global.css"/>
        '''
        head_template = '''
            <link rel="stylesheet" href="index.css"/>
        '''
        global_nav_template = '''
            <h1>Buy some art bro</h1>
        '''
        body_template = '''
            <p>Walter White's amazing art sold here</p>
        '''

        user_config_dir = self.createUserConfig(
            manifest={
                'site': {
                    'name': title,
                },
            },
            templates={
                'global-head.html': global_head_template,
                'index-head.html': head_template,
                'global-nav.html': global_nav_template,
                'index.html': body_template,
            },
        )

        # When a user requests the index page
        # pylint: disable=C0103
        c = Client()
        with self.setUserConfig(user_config_dir):
            response = c.get('/')

        # Then response code should be 200
        self.assertEqual(response.status_code, 200)

        # And should have the correct title
        self.assertContains(
            response,
            f'<title>{title}</title>',
            html=True,
        )

        # And should have the correct favicon
        self.assertContains(
            response,
            '<link rel="icon" type="image/png" href="/static/user/images/favicon.png"/>',
            html=True,
        )

        # And should contain the global head template
        self.assertContains(
            response,
            global_head_template,
            html=True,
        )

        # And should contain the index head template
        self.assertContains(
            response,
            head_template,
            html=True,
        )

        # And should contain the global nav template
        self.assertContains(
            response,
            global_nav_template,
            html=True,
        )

        # And should contain the index body template
        self.assertContains(
            response,
            body_template,
            html=True,
        )

    def test_missing_templates(self):
        """Landing page should't fail when templates are missing"""
        # Given user config with no templates
        title = 'BlueIce Art'
        user_config_dir = self.createUserConfig(
            manifest={
                'site': {
                    'name': title,
                },
            },
            templates={},
        )

        # When a user requests the index page
        # pylint: disable=C0103
        c = Client()
        with self.setUserConfig(user_config_dir):
            response = c.get('/')

        # Then the response should be successful
        self.assertEqual(response.status_code, 200)


    # pylint: disable=C0103, R0201
    def createUserConfig(self, manifest=None, templates=None):
        """Create a temporary user config directory with the supplied contents"""
        user_config_dir = tempfile.mkdtemp()
        default_dirs = {
            'templates',
            'images',
            'js',
            'css',
            'products',
        }
        for dirname in default_dirs:
            os.mkdir(os.path.join(user_config_dir, dirname))
        with open(
            os.path.join(user_config_dir, 'config.toml'),
            'w',
            encoding='utf-8',
        ) as f:
            f.write(toml.dumps(manifest or {}))
        for template_name, template in (templates or {}).items():
            with open(
                os.path.join(user_config_dir, 'templates', template_name),
            'w',
            encoding='utf-8',
        ) as f:
                f.write(template)

        return user_config_dir

    @contextmanager
    # pylint: disable=C0103
    def setUserConfig(self, user_config_dir):
        """Returns a context manager within which the user config directory
        has been overidden to the provided value"""
        with self.settings(USER_CONFIG_DIR=user_config_dir):
            importlib.reload(store_views)
            yield None
        importlib.reload(store_views)
