#### [GO TO BACK](../README.md)

# 3. Building a Static Site Generator

```python
prototypes.py  
sitebuilder  
    __init__.py  
    static/
        js/
        css/
    templates/
    urls.py
    views.py
```

##### prototypes.py
```python
import os
import sys
from django.conf import settings

BASE_DIR = os.path.dirname(__file__)
    STATIC_URL = '/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),

settings.configure(
    DEBUG=True,
    SECRET_KEY='b0mqvak1p2sqm6p#+8o8fyxf+ox(le)8&jh_5^sxa!=7!+wxj0',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'django.contrib.webdesign',
        'sitebuilder',
    ),
    STATIC_URL='/static/',
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)
```

```html
 <!DOCTYPE html>
<html lang="en"> 
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>{% block title %}Rapid Prototypes{% endblock %}</title> 
    <link rel="stylesheet" href="{% static 'css/site.css' %}">
</head>
<body>
{% block content %}{% endblock %}
</body>
</html>
```
##### views.py
```python
import os

from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template import Template
from jango.utils._os import safe_join

def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.SITE_PATES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')

    with open(file_path, 'r') as f:
        page = Template(f.read())

    return page

def page(request, slug='index'):
    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    content = {
        'slug': slug,
        'page': page,
    }
    return render(request, 'page.html', context)
```
##### urls.py
```python
from django.conf.urls import url
from .views import page

urlpatterns = (
    url(r'^(?P<slug>[\w./-]+)/$', page, name='page')
    url(r'^$', page, name='homepage'),
)
```
