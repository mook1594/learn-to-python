# Python

### 개발 환경 설치

##### Python3 설치

```shell
$ python3 -V
$ pip3 list
```

##### 가상 환경 소프트웨어 설치

```shell
$ sudo pip3 install virtualenvwrapper
```

##### 환경 변수 추가(~/.bash_profile)

```txt
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
# which virttualenvwrapper.sh
```

##### .bashrc 파일 다시 로드

`$ source ~/.bash_profile`

##### Django 설치

```shell
$ python3 install django
$ python3 -m django --version
```

##### 가상 환경 생성

```shell
$ mkdir {프로젝트 폴더} # 프로젝트 폴더 생성
$ cd {프로젝트 폴더} # 프로젝트 폴더 접근
$ virtualenv --python=python3 devenv
```

##### 가상 환경 활성화

```shell
$ source ./devenv/bin/activate
(devenv) $ # 활성화됨
$ source deactivate # 활성화 취소
```

##### django 다시 설치

```shell
$ pip install django # 새가상환경에서 장고 재설치
$ python3 -m django --version
```

##### 프로젝트 생성

```shell
$ django-admin startproject {project} .
```

##### 서버 띄우기

```shell
$ python manage.py runserver
```

##### Django 앱 생성

```shell
(devenv) $ python manage.py startapp {프로 폴더명}
```

##### Django REST framework 추가

```shell
(devenv) $ pip install djangorestframework
```

##### 셋팅 추가

- settings.py 셋팅 추가

```python
INSTALLED_APPS = [
    '{django 폴더명}',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

##### Model

- {폴더명}/models.py

```python
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=144)

    subtitle = models.CharField(blank=True, null=True, max_length=144)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return '[{}] {}'.format(self.user.username, self.title)

```

##### Serializers

```python
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'subtitle',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)
```

##### View

```python
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
```

##### Url

- {폴더}/url.py

```python
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView

post_list = PostView.as_view({
    'post': 'create',
    'get': 'list'
})

post_detail = PostView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
])
```

- url.py

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

##### migrate 실행

```shell
(devenv) $ python manage.py makemigrations
(devenv) $ python manage.py migrate
(devenv) $ python manage.py runserver
```
