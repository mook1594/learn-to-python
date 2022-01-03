#### [GO TO BACK](../README.md)

# 7. 쿼리와 데이터베이스 레이어
- ORM은 데이터베이스 종류와 독립적인 형태로 객체화
- ORM에서 예기치 못한 문제를 피하기 위해 아래를 이용해보자

## 7.1 단일 객체에서 get_object_or_404() 이용하기
- get_object_or_404()는 뷰에서만 이용

## 7.2 예외를 일으킬 수 있는 쿼리를 주의하자
- get_object_or_404()를 이용하면 try-except 블록을 이용할 필요가 없지만 다른 경우엔 필요하다
### ObjectDoesNotExist와 DoesNotExist
``` python
from django.core.exceptions import ObjectDoesNotExist

from flavors.models import Flavor
from store.exceptions import OutOfStock

def list_flavor_line_item(sku):
    try:
        return Flavor.objects.get(sku=sku, quantity__gt=0)
    except Flavor.DoesNotExist:
        msg = "we are out of {0}".format(sku)
        raise OutOfStock(msg)
    
def list_any_line_item(model, sku):
    try:
        return model.objects.get(sku=sku, quantity__gt=0)
    except ObjectDoesNotExist:
        msg = "we are out of {0}".format(sku)
        raise OutOfStock(msg)

```
### 여러 개의 객체가 반환되었을 때
쿼리가 하나 이상의 객체를 반환할 수도 있다면 MultipleObjectsReturned 예외를 참고
``` python
from flavors.models import Flavor
from stroe.exceptions import OutOfStock, CorruptedDatabase

def list_flavor_line_item(sku):
    try:
        return Flavor.objects.get(sku=sku, quantity__gt=0)
    except Flavor.DoesNotExist:
        msg = "we are out of {}".format(sku)
    except Flavor.MultipleObjectsReturned:
        msg = "Multiple items have SKU {}. Please fix!".format(sku)
        raise CorruptedDatabase(msg)
```

## 7.3 쿼리를 좀 더 명확하게 하기 위해 지연 연산 이용하기
- ORM의 나쁜 예제
``` python
from django.models import Q

from promos.models import Promo

def fun_function(**kwargs):
    """유효한 아이스크림 프로모션 찾기"""
    # 너무 길게 작성된 쿼리 체인은 피하자
    return Promo.objects.active().filter(Q(name__startswith=name) |
                                        Q(description__icontains=name))
```
- 지연 연산(lazy evaluation)을 이용하자 
``` python
from django.models import Q

from promos.models import Promo

def fun_function(**kwargs):
    results = Promo.objects.active()
    results = results.filter(
        Q(name__startwith=name) |
        Q(description__icontains=name)
    )
    results = results.exclude(status='melted')
    results = results.select_related('flavors')
    return results
```

## 7.4 고급 쿼리 도구 이용하기
- 데이터를 뽑아 파이썬에서 데이터를 가공할 것인가? 가공된 데이터를 뽑을 것인가? 어떤것이 성능적으로 유리할까?
- 장고의 고급 쿼리 도구를 이용해보자
### 쿼리 표현식 (query expression)
- 쿼리 표현식 사용 전
``` python
from models customers import Customer

customer = []
for customer in Customer.objects.iterate():
    if customer.scoops_ordered > customer.store_visits:
        customers.append(customer)
```
- 데이터베이스 안에 모든 레코드에 대해 하나하나 for루프가 돌아 느리고, 메모리도 차지
- 코드 자체 경합(race condition)이 발생. update가 동시에 일어나게되면...
- 쿼리 표현식을 사용해보자
``` python
from django.db.models import F
from models.customers import Customer
customers = Customer.objects.filter(scoops_ordered__gt=F('store_visits'))

# SELECT * FROM customers_customer WHERE scoops_ordered > store_visits
```
- [쿼리 표현식에 대한 참고 자료](https://docs.djangoproject.com/ko/4.0/ref/models/database-functions/)

### 데이터베이스 함수들
- UPPER(), LOWER(), COALESCE(), CONCAT(), LENGTH(), SUBSTR() 등 사용가능

## 7.5 필수불가결한 상황이 아니라면 로우 SQL은 지향하자
- ORM(Object-Relational Model)을 사용하는 이유는 다양한 환경에서 단순한 쿼리 작성 및 모델에 대한 접근과 업데이트를 할 때 유효성 검사와 보안을 제공
- 최대한 ORM을 이용할 것
- 그럼 언제 로우 SQL을 이용하나?  
: ORM을 통한 것 보다 훨씬 간결해지고 단축되는 경우만 사용.

## 7.6 필요에 따라 인덱스를 이용하자
- 인덱스 추가 `db_index=True`
- 인덱스를 추가해야하는 경우
    - 인덱스가 빈번하게 이용될 때 (모든 쿼리의 10~25% 사이)
    - 실제 데이터 또는 실제와 비슷한 데이터가 존재해서 인덱싱 결과에 대한 분석이 가능할 때
    - 인덱싱을 통해 성능이 향상되는지 테스트할 수 있을 때

## 7.7 트랜잭션
- 둘 또는 그 이상의 데이터베이스 업데이트를 단일화된 작업으로 처리하는 기법
- ACID: 원자성(atomic), 일관성(consistent), 독립성(isolated), 지속성(durable)
### 각각의 HTTP 요청을 트랜잭션으로 처리하는 설정
``` python
# settings/base.py

DATABASES = {
    'default': {
        #...
        'ATOMIC_REQUESTS': True,
    },
}
```
- 모든 데이터베이스 쿼리가 보호되는 안전성을 얻을 수 있는 장점
- 성능 저하의 단점(locking에 따라)
- 트랜젝션을 피하고 싶다면 `non_automic_requests()`를 활용
``` python
@transaction.non_atomic_requests
def posting_flavor_status(request, pk, status):
    flavor = get_object_or_404(Flavor, pk=pk)

    # 오토 커밋 모드 실행
    flavor.lastest_status_change_attempt = timezone.now()
    flavor.save()

    with transaction.atomic():
        # 트랜젝션 안에서 실행
        flavor.status = status
        flavor.latest_status_change_success = timezone.now()
        flavor.save()
        return HttpResponse('Hooray')

    # 트랜젝션이 실패하면 상태 코드 반환
    return HttpResponse('Sadness', status_code=400)
```

### 명시적 트랜잭션 선언 (explicit transaction declaration)
- 성능 문제가 정말 심각 하지 않으면 ATOMIC_REQUESTS를 이용하라
- 데이터베이스에 변경이 생기지 않는 작업은 트랜잭션으로 처리하지 말자
- 데이터베이스에 변경이 생기는 작업은 반드시 트랜잭션으로 처리
- 읽기 작업을 수반하는 변경작업이면 (성능이나) 고려해보자

### django.http.StreamingHttpResponse와 트랜잭션
- 뷰가 StreamingHttpResponse를 반환한다면 response가 시작된 이상 트랜잭션 에러를 처리하기 힘듬

### MySQL에서 트랜잭션
- 데이터베이스 타입이 InnoDB냐 MyISAM이냐에 따라 다르다.

### [장고 트랜잭션 관련 참고 자료](https://docs.djangoproject.com/ko/4.0/topics/db/transactions/)
### [RealPython 트랜잭션](https://realpython.com/transaction-management-with-django-1-6/)
