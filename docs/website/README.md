```shell
$ mkdir {folder}
$ cd {folder}
$ django-admin startproject config .
$ django-admin startapp {app}
```

##### config/urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iamport/', include('iamport.urls')),
]
```
##### app/urls.py
```python
from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('index', views.index)
]
```
##### app/views.py
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("테스트")
```
### Html 추가
```
mysite
--- config
--- app
--- templates << (생성)
--- --- app
--- --- --- index.html
```
##### app/views.py
```python
from django.shortcuts import render

def index(request):
    return render(request, 'iamport/index.html', {})
```
