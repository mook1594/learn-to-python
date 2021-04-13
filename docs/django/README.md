#### [GO TO BACK](../README.md)

### Django REST Framework

### 코드 구성

#### urls.py

```python
from django.urls import path
from qualson_admin.coupon.views import *
from rest_framework import renderers

urlpatterns = [
    path('coupon/code-factory/<int:id>', CouponFactoryIdView.as_view()),
    path('coupon/code-factory/list', CouponFactoryView.as_view()),
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
class CouponFactoryView(views.APIView):
    # 커스텀 인증 방식
    authentication_classes = ()
    permission_classes = (AcceptSpringTokenPermission,)

    def get(self, request, *args, **kwargs):
        codeFactory = CodeFactory.objects.all()
        serializer = CodeFactorySerializer(codeFactory, many=True)
        return Response(data = serializer.data, status=status.HTTP_200_OK)

```

##### GET

```python
class CouponFactoryIdView(views.APIView):
    # 커스텀 인증 방식
    authentication_classes = ()
    permission_classes = (AcceptSpringTokenPermission,)

    def get(self, request, id:int, *args, **kwargs):
        codeFactory = CodeFactory.objects.get(id = id)
        serializer = CodeFactorySerializer(codeFactory, many=False)
        return Response(data = serializer.data, status=status.HTTP_200_OK)
```

##### POST

```python
class CouponFactoryView(views.APIView):
    authentication_classes = ()
    permission_classes = (AcceptSpringTokenPermission,)

    def post(self, request, *args, **kwargs):
        serializer = CodeFactorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
```

##### PUT

```python
class CouponFactoryIdView(views.APIView):
    authentication_classes = ()
    permission_classes = (AcceptSpringTokenPermission,)

    def put(self, request, id:int, *args, **kwargs):
        codeFactory = CodeFactory.objects.get(id=id)
        serializer = CodeFactorySerializer(instance=codeFactory, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
```

##### DELETE

```python
class CouponFactoryIdView(views.APIView):
    authentication_classes = ()
    permission_classes = (AcceptSpringTokenPermission,)

    def delete(self, request, id:int, *args, **kwargs):
        codeFactory = CodeFactory.objects.get(id=id)
        codeFactory.delete()
        return Response(data = True, status=status.HTTP_200_OK)
```
