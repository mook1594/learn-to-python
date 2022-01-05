#### [GO TO BACK](../README.md)

# 9. 함수 기반 뷰의 모범적인 이용

## 9.1 함수 기반 뷰의 장점
- 뷰 코드는 작을 수록 좋다
- 뷰에서 절대 코드를 반복해서 사용하지 말자
- 뷰는 프레젠테이션 로직을 처리해야 한다. 비즈니스 로직은 가능한 한 모델 로직에 적용시키고 만약 해야 한다면 폼 안에 내재시켜야 한다.
- 뷰를 가능한 한 단순하게 유지하자
- 403, 404, 500을 처리하는 커스텀 코드를 쓰는데 이용하라
- 복잡하게 중첩된 if 블록 구문을 피하자

## 9.2 HttpRequest 객체 전달하기
- django.http.HttpRequest 유틸 함수를 이용
``` python
# utils.py
from django.core.exceptions import PermissionDenied

def check_sprinkle_rights(request):
    if request.user.can_sprinkle or request.user.is_staff:

        # 이 내용을 여기 첨부함으로써 템플릿을 좀 더 일반적으로 이용
        request.can_sprinkle = True

        return request

    # HTTP 403을 사용자에게 반환
    raise PermissionDenied
```

## 9.3 편리한 데코레이터
``` python
import functools

def decorator(view_func):
    @functools.wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        # 여기에서 request(HTTPRequest) 객체를 수정하면 된다.
        response = view_func(request, *args, **kwargs)
        # 여기에서 response(HttpResponse) 객체를 수정하면 된다.
        return response
    return new_view_func
```
- 예제
``` python
from functools import wraps

from . import utils

def check-sprinkles(view_func):
    """사용자가 스프링클을 추가할 수 있는지 확인한다 """
    @wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        # request 객체를 utils.can_sprinkle()에 넣는다.
        request = utils.can_sprinkle(request)

        # 뷰 함수를 호출
        response = view_func(request, *args, **kwargs)

        # HttpResponse 객체를 반환
        return response
    return new_view_func
```

### 데코레이터 남용하지 않기
- 데코레이터를 여러개 만들어 복잡하게 얽힌 관계를 만들지 말자