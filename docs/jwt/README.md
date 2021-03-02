#### [GO TO BACK](../README.md)

# JWT

#### 장고, jwt 설치

```shell
$ pip install djangorestframework djangorestframework-jwt
```

```shell
$ pip freeze > requirements.txt
```

#### JWT 설정

##### {프로젝트}/settings.py

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    )
}

JWT_AUTH = {
    'JWT_SECRET_KEY': 'SECRET-KEY',
    'JWT_ALGORITHM': 'HS256',
    'JWT_ALLOW_REFRESH': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(day=7),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=28),
}
```

#### View 만들기

```python
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Post

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((JSONWebTokenAuthentication,))
def posts(request):
    posts = Post.objects.filter(
        published_at_isnull=False).order_by('-published_at')
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")
```
