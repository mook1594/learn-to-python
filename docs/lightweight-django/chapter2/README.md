#### [GO TO BACK](../README.md)

# 2. Stateless Web Application
```shell
$ django-admin.py startproject placeholder --template=project_name
```
##### manage.py
```python
import os
import sys

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
SECRET_KEY = os.environ.get('SECRET_KEY', '%jv_4#hoaqwig2gu!eg#^ozptd*a@88u(aasv7z!7xt^5(*i&k')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDOLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles', 
    ),
    TEMPLATE_DIRS=(
        os.path.join(BASE_DIR, 'templates'),
    ), STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'), 
    ),
    STATIC_URL='/static/',
)

```
##### Views
```python
def placeholder(request, width, height):
    # TODO: Rest of the view will go here
    return HttpResponse('Ok')

def index(request):
    return HttpResponse('Hello World')
```
##### Url Patterns
```python
urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
    url(r'^$', index, name='homepage')
)
```
##### Placeholder View
```python
import hashlib
import os

from django import forms
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import etag
from PIL import Image, ImageDraw


class ImageForm(forms.Form):
    """Form to validate requested placeholder image"""

    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)
    
    def generate(self, image_format='PNG'):
        """Generate an image of the given type and return as raw bytes."""
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        
        key = '{}.{}.{}'.format(width, height, image_format)
        content = cache.get(key)
        
        if content is None:
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            text = '{} X {}'.format(width, height)
            textwidth, textheight = draw.textsize(text)
            if textwidth < width and textheight < height:
                texttop = (height - textheight) // 2
                textleft = (width-textwidth) // 2
                draw.text((textleft, texttop), text, fill=(255, 255, 255))
            content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            cache.set(key, content, 60 * 60)
         return content


def generate_etag(request, width, height):
    content = 'Placeholder: {0} x {1}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


@etag(generate_etag)
def placeholder(request, width, height):
    form = ImageForm({'height':height, 'width':width})
    if form.is_valid():
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
    else
        return HttpResponseBadRequest('Invalid Image Request')


def index(request):
    example = reverse('placeholder', kwargs={'width': 50, 'height: 50})
        context = {
        'example': request.build_absolute_uri(example)
    }
    return render(request, 'home.html', context)


urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
    url(r'^$', index, name='homepage'),
)

application = get_wsgi_application()

if __name__=='__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
```
##### html
```html
  {% load staticfiles %}
<!DOCTYPE html>
<html lang="en"> <head>
    <meta charset="utf-8">
    <title>Django Placeholder Images</title>
    <link rel="stylesheet" href="{% static 'site.css' %}" type="text/css">
</head>
<body>
<h1>Django Placeholder Images</h1>
<p>This server can be used for serving placeholder
    images for any web page.</p>
<p>To request a placeholder image of a given width and height simply include an image with the source pointing to <b>/placeholder/&lt;width&gt;x&lt;height&gt;/</b>
    on this server such as:</p>
<pre>
&lt;img src="{{ example }}" &gt; </pre>
<h2>Examples</h2> <ul>
    <li><img src="{% url 'placeholder' width=50 height=50 %}"></li> <li><img src="{% url 'placeholder' width=100 height=50 %}"></li> <li><img src="{% url 'placeholder' width=50 height=100 %}"></li>
    <ul>
</body>
</html>

body {
    text-align: center;
}
ul {
    list-type: none;
}
li {
    display: inline-block;
}
```

