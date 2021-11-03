"""View methods for backoffice"""

from artisanutils import get_user_template, get_manifest_file

from django.http import HttpResponse
from django.template import Template, RequestContext


INDEX_TEMPLATE = Template(f"""
{{% load static %}}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <link rel="icon" type="image/png" href="{{% static 'user/images/favicon.png' %}}"/>
    <title>{ get_manifest_file().get('site', {}).get('name') }</title>
    {get_user_template('global-head.html')}
    {get_user_template('index-head.html')}
  </head>
  <body>
    {get_user_template('global-nav.html')}
    {get_user_template('index.html')}
  </body>
</html>
""")


def index(request):
    """Simple index view"""
    context = RequestContext(
        request,
        {
            'designer_url': 'https://google.com',
        },
    )
    return HttpResponse(INDEX_TEMPLATE.render(context))
