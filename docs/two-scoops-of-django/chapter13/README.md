#### [GO TO BACK](../README.md)

# 13. 템플릿의 모범적인 이용
## 13.1 대부분의 템플릿은 templates/에 넣어 두자
## 13.2 템플릿 아키텍처 패턴
- 모든 템플릿은 하나의 base.html로 부터 상속받아 생성
### 2중 템플릿 구조의 예
``` python
templates/
    base.thml
    dashboard.html # base.html 확장
    profiles/
        profile_detail.html # base.html 확장
```
### 3중 템플릿 구조의 예
``` python
templates/
    base.thml
    dashboard.html # base.html 확장
    profiles/
        base_profiles.html # base.html 확장
        profile_detail.html # base_profiles.html 확장
```
## 13.3 템플릿에서 프로세싱 제한하기
### 주의 사항 1: 템플릿 상에서 처리하는 aggregation 메서드
- 이터레이션 연산에 주의
``` python
<tbody>
    {% for age_bracket in age_brackets %}
    <tr>
        <td>{{ age_bracket.title }}</td>
        <td>{{ age_bracket.count }}</td>
    </tr>
    {% endfor %}
</tbody>
```
- ORM의 aggregation 메서드를 이용한다
``` python
# managers.py
from django.utils import timezone

from dateuil.relativedelta import relativedelta

from django.db import models

class VoucherManager(models.Manager):
    def age_breakdown(self):
        """연령대별 카운트 수를 저장한 딕셔너리 반환 """
        age_brackets = []
        now = timezone.now()

        delta = now - relativedelta(years=18)
        count = self.model.objects.filter(birth_date__gt=delta).count()
        age_brackets.append(
            {'title': '0-17', 'count': count}
        )
        age_brackets.append(
            {'title': '18+', 'count': count}
        )
        return age_brackets
```

### 주의 사항 2: 템플릿상에서 조건문으로 하는 필터링
- 템플릿에서 루프문을 돌면서 if문으로 찾지 말자
``` python
from django.views.generic import TemplateView

from .models import Voucher

class GreenfeldRoyView(TemplateView):
    template_name = 'vouchers/views_conditional.html';

    def get_context_data(self, **kwargs):
        context = super(GreenfeldRoyView, self).get_context_data(**kwargs)
        context['greenfelds'] = Voucher.objects.filter(name__icontains='greenfeld')
        context['roys'] = Voucher.objects.filter(name__icontains='roy')
        return context
```

### 주의 사항 3: 템플릿상에서 복잡하게 얽힌 쿼리들
``` html
# 나쁜 예제
{% for user in user_list %}
    <li>
        {{ user.name }}:
        {# 암묵 적인쿼리 사용하지말자 #}
        {{ user.flavor.title }}
        {{ user.flavor.scoops_remaining }}
    </li>
{% endfor %}
```

``` html
{% comment %}
List generated via User.object.all().selected_related('flavors')
{% endcomment %}
# 수정
{% for user in user_list %}
    <li>
        {{ user.name }}:
        {# 암묵 적인쿼리 사용하지말자 #}
        {{ user.flavor.title }}
        {{ user.flavor.scoops_remaining }}
    </li>
{% endfor %}
```
### 주의 사항 4: 템플릿에서 생기는 CPU 부하
- 많은 양의 이미지나 데이터를 처리하는 곳은 비동기 메시지 큐 시스템 처리

### 주의 사항 5: 템플릿에서 숨겨진 REST API 호출
- REST API를 어디서 호출해야할까?
    - 자바스크립트 코드: 브러우저에서 자바스크립트로 처리한다.
    - 느린 프로세스를 메시지 큐, 스레드, 멀티프로세스 등으로 처리하는 코드

## 13.4 HTML 코드를 정돈하는데 너무 신경 쓰지 말라

## 13.5 템플릿의 상속
``` html
<!-- base.html -->
{% load staticfiles %}
<html>
    <head>
        <title>
            {% block title %}Two Scoops of Django{% endblock title %}
        </title>
        {% block stylesheets %}
            <link rel="stylesheet" type="text/css" href="{% static 'css/project.css' %}">
        {% endblock stylesheets %}
    </head>
    <body>
        <div class="content">
            {% block content %}
                <h1>Two Scoops</h1>
            {% endblock content %}
        </div>
    </body>
</html>
```
### 탬플릿 태그
- {% load %}: 정적 파일의 내장 템플릿 태그 라이브러리를 로드
- {% block %}: 오버라이드 가능한 영역으로 지정
- {% static %}: 정적 미디어 인자
``` python
# 상속을 통한 about.html
{% extends "base.html" %}
{% load staticfiles %}
{% block title %}About Audrey and Daniel{% endblock title %}
{% block stylesheets %}
    {{ block.super }}
    <link rel="stylesheet" type="text/css" href="{% static 'css/about.css' %}">
{% endblock stylesheets %}
{% block content %}
    {{ block.super }}
    <h2> About Audery and Daniel</h2>
    <p>They enjoy eating ice cream</p>
{% endblock content %}
```
### 템플릿 객체
- {% extends %}: 장고에게 상속 됨을 알려줌
- {% block %}: 오버라이드 영역 지정
- {{ block.super }}: 부모 블록 안의 내용 사용


## 13.6 강력한 기능의 block.super

## 13.7 그 외의 유용한 사항들
### 파이썬 코드와 스타일을 긴밀하게 연결하지 않도록 한다.
- 디자인 레이아웃과 관련된 상수들은 CSS에서 관리
### 일반적인 관례
- 템플릿, 블록, 이름등은 (_)을 선호
- 직관적인 블록이름 {% block javascript %}을 사용하도록한다
- 맺음 블록 이름을 명확하게 한다 {% endblock %} 보다는 {% endblock javascript %}
### 템플릿의 위치
- 일반적으로 템플릿 폴더에 전부 위치
- 예외, 서드파티 패키지에 앱을 번들하는 경우 앱 안에 위치
### 콘텍스트 객체에 모델의 이름을 붙여 이용하기
- {{ object_list }}, {{ object }}
### 하드 코딩된 경로 대신 URL 이름 이용하기
- `<a href="/flavor">` 대신 `<a href="{% url 'flavors_list' %}">`을 사용
### 복잡한 템플릿 디버깅하기
``` python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS':
            'string_if_invalid': 'INVALID EXPRESSION: %s'
    },
]
```

## 13.8 에러 페이지 템플릿
- 정적인 404, 500에 대한 페이지를 만들자

## 13.9 미니멀리스트 접근법을 따르도록 한다.
