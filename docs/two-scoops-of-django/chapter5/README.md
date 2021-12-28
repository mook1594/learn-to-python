#### [GO TO BACK](../README.md)

# 5. settings와 requirements 파일
## 5.1 버전 관리되지 않는 로컬 세팅은 피하도록 한다
- local_settings는 안티 패턴이지만, 비밀 정보를 보호하기 위해선 필요한것도 같다
- 서버의 암호 정보 등은 버전 컨트롤에서 빼서 관리하는 것이 중요
- 다음의 방법으로 이용

## 5.2 여러 개의 settings 파일 이용하기
- 한 개의 settings.py를 이용하기 보단 settings 아래 여러개의 셋업 파일을 구성하여 이용
```
settings/
    __init__.py
    base.py
    local.py
    statging.py
    test.py
    production.py
```
- 위 처럼 구성하게되면 장고 실행에서는 다음과 같다
``` shell
$ python manage.py runserver --settings=twoscoops.settings.local
```
- DJANGO_SETTINGS_MODULE을 설정 해야 한다
- virtualenv의 postactivate 스크립트에 DJANGO_SETTINGS_MODULE, PYTHONPATH를 설정하면 옵션없이 자동 적용

### 개발 환경의 settings 파일 예제
- settings/local.py
``` python
from .base import *

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'twoscoops',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',

    }
}
INSTALLED_APPS += ('debug_toolbar,',)
```

### 다중 개발 환경 세팅
- settings/dev_pydanny.py
``` python
from .local import *

CACHE_TIMEOUT = 30
```

## 5.3 코드에서 설정 분리하기
### 환경 변수에 비밀 키 등을 넣어 두기 전에 유의할 점
- 저장되는 비밀 정보를 관리할 방법
- 서버에서 bash가 환경 변수와 작용하는 방식에 대한 이해 또는 Paas 이용 여부

### 로컬 환경에서 환경 변수 세팅하기
- bash를 이용하는 경우 bashrc, .bash_profile, .profile 뒷부분에 추가
``` bash
$ export SOME_SECRET_KEY=1234alsdf15134
$ export AUDREY_FREEZER_KEY=sldk-3kj421-kjkjv-3434
```
- 윈도우 일 경우는 set 명령어로 해주어야하는데, 쉬운방법으로는 virtualenv의 bin/activate.bat 스트립트 아래 부분에 추가하면 활성화되면서 실행된다
``` cmd
> set SOME_SECRET_KEY 102945k2jtl21f
```

### 운영 환경에서 환경 변수를 세팅하는 방법
- 허로쿠(Heroku)를 기반한 설정
``` shell
$ heroku config:set SOME_SECRET_KEY=2lijbl2lkjcv90fd5
```
- 파이썬에서 설정된 환경변수를 접근하려면
``` shell
# 파이썬 프롬프트
>>> import os
>>> os.environ['SOME_SECRET_KEY']
'sldkfsldkfsdfj'
```
- 세팅파일에서 환경변수에 접근하려면
``` python
# settings/production.py
import os
SOME_SECRET_KEY = os.environ['SOME_SECRET_KEY']
```

### 비밀 키가 존재하지 않을 때 예외 처리하기
- 환경변수가 설정이 안되어있거나 설정이 여의치 않을때 대응할 수 있는 코드
``` python
import os

from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    """ 환경 변수를 가져오거나 예외를 반환한다."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(erro.r_msg)

SOME_SECRET_KEY = get_env_variable('SOME_SECRET_KEY')
```

## 5.4 환경 변수를 이용할 수 없을 때
- 아파치 웹(HTTP) 서버로 이용하는 경우, Nginx 기반 환경에서도 특정 경우
- 비밀 파일 패턴 (secrets file pattern) 이용  
: 장고에서 실행되지 않는 형식의 파일을 버전 컨트롤 시스템에 추가하지 않고 사용하는 방법  
(json, config, yaml, xml)
``` json
{
    'FILENAME': 'secrets.json',
    'SECRET_KEY': 'I've got a secret!',
    'DATABASES_HOST': '127.0.0.1',
    'PORT': '5432'
}
```
- settings에 해당 파일 import
``` python
import json

with open('secrets.json') as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret('SECRET_KEY')
```

## 5.5 여개 개의 requirements 파일 이용하기
- 패턴
```
<repository_root>
    requirements/
        base.txt
        local.txt
        staging.txt
        production.txt
```
- base.txt
``` text
Django==4.0
psyconpg2==2.6
djangorestframework==3.1.1

```
- local.txt
```
-r base.txt
coverage==3.7.1
django-debug-toolbar==1.3.0
```

### 여러 개의 requirements 파일로 부터 설치하기
``` shell
$ pip install -r requirements/local.txt
$ pip install -r requirements/production.txt
```

### 여러 개의 requirements 파일을 Paas 환경에서 이용하기
- [Paas 배포](../chapter30/README.md)

## 5.6 settings에서 파일 경로 처리하기
- 장고 세팅 파일에 하드 코딩된 파일 경로(고정 경로)를 넣지 말자!
- BASE_DIR을 활용하여 세팅 하기
``` python
from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = BASE_DIR.child('media')
STATIC_ROOT = BASE_DIR.child('static')
STATICFILES_DIRS = (
    BASE_DIR.child('assets')
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        DIRS = (BASE_DIR.child('templates'),)
    }
]
```
``` python
from os.path import join, abspath, dirname
here = lambda *dirs: join(abspath(dirname(__file__)), *dirs)
BASE_DIR = here("..", "..")
root = lambda *dirs: join(abspath(BASE_DIR), *dirs)

#MEDIA_ROOT 설정
MEDIA_ROOT = root('media')
STATIC_ROOT = root('collected_static')
STATICFILES_DIRS = (
    root('assets'),
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jango.DjangoTemplates',
        DIRS = (root('templates'),)
    }
]
```

- 장고 세팅이 기본 장고 세팅과 다르게 되어있는지 확인하고 싶으면 장고 관리 콘솔에서 `diffsettings` 명령어 입력