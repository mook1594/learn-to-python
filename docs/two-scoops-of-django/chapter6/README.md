#### [GO TO BACK](../README.md)

# 6. 장고에서 모델 이용하기
### 모델을 작업하면서 이용하는 장고 패키지들
- django-model-utils: TimeStampedModel 처리를 용이하게함
- django-extensions: shell_plus 관리 명령어 제공

## 6.1 시작하기
### 모델이 너무 많으면 앱을 나눈다
### 모델 상속에 주의
- 추상화 기초 클래스 (abstract base class)
- 멀티테이블 상속 (multi-table inheritance)
- 프락시 모델 (proxy model)
### 실제로 모델 상속해 보기
- TimeStampedModel
``` python
from django.db import models

class TimeStampedModel(models.Model):
    """
    'created'와 'modified' 필드를 자동으로 업데이트해 주는 추상화 기반 클래스 모델
    """
    created = models.DateTimeField(auto_now_add=True)
    midified = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Flavor(TimeStampedModel):
    title = models.CharField(max_length=200)
```
### 데이터베이스 마이그레이션

## 6.2 장고 모델 디자인
- 좋은 장고 모델 디자인하기
### 정규화 하기
- 정규화 (database normalization)에 익숙해지자
- [참고 자료1](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4_%EC%A0%95%EA%B7%9C%ED%99%94)
- [참고 자료2](https://ko.wikipedia.org/wiki/%EC%A0%9C1%EC%A0%95%EA%B7%9C%ED%98%95)
### 캐시와 비정규화

### 반드시 필요한 경우에만 비정규화를 하도록 하자
- 비정규화를 하기전에 캐싱을 고려해보자
- [24장 장고 성능 향상시키기](../chapter24/README.md)에서 제시한 방법으로 해결할 수 없다면 비정규화를 고려해보자

### 언제 널을 쓰고 언제 공백을 쓸 것인가
- balck=True를 사용하는 경우  
: CharField, TextField, SlugField, EmailField, CommaSeparatedIntegerField, UUIDField, FileField, ImageField
- 둘다 사용하지 않는 경우  
: BooleanField, IPAddressField
- null=True를 사용하는 경우  
: IntegerField, FloatField, DecimalField, DurationField
- null=True를 이용하면서 auto_now, auto_now_add를 같이 활용  
: DateTimeField, DateField, TimeField
- 둘다 사용  
: ForeignKey, ManyToManyField, OneToOneField, GenericIPAddressField
> IPAddressField 보단 GenericIPAddressField를 이용하자

### 언제 BinaryField를 이용할 것인가
- 메시지팩 형식의 콘텐츠
- 원본 센서 데이터
- 압축된 데이터.
> 바이너리 데이터는 크기가 방대하고 그로인해 데이터베이스가 느려질 수 있다.  
> 데이터베이스의 읽기/쓰기 속도는 파일시스템의 읽기/쓰기 속도보다 느리다

### 범용 관계 피하기
- 범용 관계 (Generic relations)
: 한 테이블로 부터 다른 테이블을 서로 제약 조건이 없는 외부 키(GenericForeignKey)로 바인딩 한것
- 모델간 인덱싱이 존재하지 않으면 쿼리 속도에 손해를 가져오게 된다.
- 다른 테이블에 존재하지 않는 레코드를 참조할 수 있는 데이터 충돌의 위험성이 존재

## 6.3 모델의 _meta API
### _meta 기능이 필요할때
- 모델 필드의 리스트를 가져올 때
- 모델의 특정 필드의 클래스를 가져올 때(상속 관계나 상속 등을 통해 생성된 정보를 가져올때 도)
- 장고 버전들에서 이러한 정보의 원천을 확실하게 상수로 남기기 원할 때
- [관련 문서](https://docs.djangoproject.com/ko/4.0/ref/models/meta/)

## 6.4 모델 매니저
- [참고 문서](https://docs.djangoproject.com/ko/4.0/topics/db/managers/)
``` python
from django.db import models
from django.utils import timezone

class PublishedManager(models.Manager):
    
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(pub_date__lte=timezone.now(), **kwargs)


class FlavorReview(models.Model):
    review = models.CharField(max_length=255)
    pub_date = models.DateTimeField()

    objects = PublishedManager()
    # 디폴트 objects = models.Manager()
```

## 6.5 거대 모델 이해하기
- 거대 모델 (fat Model)   
: 관련 코드를 뷰나 템플릿에 넣기 보다 모델 메서드, 프로퍼티 등등에 넣어 캡슐화 하는 것
### 거대 모델 예
- 아이스크림 리뷰를 보여주는 모델
    - Review.create_view(cls, user, rating, title, description)  
    : 리뷰를 생성하는 클래스 메서드. HTML, REST view 호출
    - review.product_average  
    : 리뷰된 프로젝트 평균 점수 반환 하는 속성
    - review.found_useful(self, user, yes)  
    : 해당 리뷰가 유용했는지 아닌지 사용자가 기록할 수 있는 메서드

- 괜찮은 방법 같지만 신의 객체 (god object) 수준으로 증가할 수 도 있음. 코드를 분리하여 작성

### 모델 행동 (model behavior / 믹스인)
- 캡슐화와 구성화의 개념.
- [참고 자료1](https://kyunooh.github.io/django/2016/10/09/%EC%9E%A5%EA%B3%A0-%EB%AA%A8%EB%8D%B8-%ED%96%89%EB%8F%99(Django-Model-Behaviors)-By-Kevin-Stone.html)
- [10.2 클래스 기반 뷰와 믹스인 이용하기](../chapter10/README.md)

### 상태 없는 헬퍼 함수

### 모델 행동과 헬퍼 함수