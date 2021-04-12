#### [GO TO BACK](../README.md)

### Django REST Framework

### 코드 구성

#### urls.py

```python
from django.urls import path
from qualson_admin.coupon.views import *
from rest_framework import renderers

urlpatterns = [
    path('coupon/code-factory/<int:id>', CouponFactoryView.as_view()),
    path('coupon/code-factory/list', CouponFactoryListView.as_view()),
]
```

#### serializers.py

```python
from rest_framework import serializers
from qms_db.models import CodeFactory

class CodeFactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeFactory
        fields = '__all__'
```

#### views.py

##### import

```python
from rest_framework import serializers, views, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from qualson_admin.permissions import AcceptSpringTokenPermission
from .serializers import CodeFactorySerializer
from qms_db.models import CodeFactory
```

##### GET - LIST

```python
class CouponFactoryListView(views.APIView):
    # 커스텀 인증방식
    authentication_classes = ()
    permission_classes = (AcceptSpringTokenPermission,)

    def get(self, request, *args, **kwargs):
        tasks = CodeFactory.objects.all()
        serializers = CodeFactorySerializer(tasks, many=True)
        return Response(data = serializers.data, status=status.HTTP_200_OK)

```

##### GET

```python
class CouponFactoryView(views.APIView):
    authentication_classes = ()
    permission_classes = (AcceptSpringTokenPermission,)

    def get(self, request, id:int, *args, **kwargs):
        tasks = CodeFactory.objects.get(id = id)
        serializers = CodeFactorySerializer(tasks, many=False)
        return Response(data = serializers.data, status=status.HTTP_200_OK)
```
