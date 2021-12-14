#### [GO TO BACK](../README.md)

# 1. 코딩 스타일
## 1.1 읽기 쉬운 코드를 만드는 것이 왜 중요한가
### 개발자의 뇌를 덜 피곤하게 하는 것이 중요
### 읽기 쉬운 코드를 만들기 위해서는
- 축약적이거나 함축적인 변수명은 피한다.
- 함수 인자의 이름들은 꼭 써 준다.
- 클래스와 메서드를 문서화 한다.
- 코드에 주석은 꼭 달도록 한다.
- 재사용 가능한 함수 또는 메서드 안에서 반복되는 코드들은 리팩터링을 해둔다.
- 함수와 메서드는 가능한 한 작은 크기를 유지한다. 어림잡아 스크롤 없이 읽을 수 있는 길이가 적합하다.

## 1.2 PEP 8
- PEP8 이란?  
: [파이썬 공식 스타일 가이드](https://pep8.org/)
### PEP8에서 코딩 관례
- 들여쓰기는 스페이스 네칸 이용
- 최상위 함수와 클래스 선언 사이는 두 줄로 구분
- 클래스 안에 메서드들은 한 줄로 구분
### flake8로 Lint 해보기
### 코드의 텍스트는 79를 넘기지 말자 (길면 99)

## 1.3 임포트에 대해
### 임포트의 종류
- 표준 라이브러리 임포트
- 연관 외부 라이브러리 임포트
- 로컬 애플리케이션 또는 라이브러리에 한정된 임포트

### 임포트의 순서
- 표준 라이브러리 임포트
- 코어 장고 임포트
- 장고와 무관한 외부 앱 임포트
- 프로젝트 앱 임포트
``` python
#표준 라이브러리 임포트
from __future__ import absolute_import
from math import sqrt
from os.path import abspath
# 코어 장고 임포트
from django.db import models
from django.utils.translation import ugettext_lazy as _
# 서드 파티 앱 임포트
from django_extensions.db.models import TimeStampedModel
# 프로젝트 앱 임포트
from splits.models import BananaSplit
```

## 1.4 명시적 성격의 상대 임포트 이용하기
### 명시적 성격의 상대 임포트 (explicit relative import)  
: 모듈 패키지를 하드코딩 하거나 구조적 종속 모듈을 분리 하는경우를 피할 수 있음
``` python
# 절대적인 임포트 보다는
from cons.models import WaffleCone
from cons.forms import WaffleConeForm
# 상대적인 임포트를 사용하자!
from .models import WaffleCone
from .forms import WaffleConeFrom

```

## 1.5 import * 는 피하자
- 기존 것 위에 덮여 로딩되어 예상치 못한 상황이 발생할 수 있다.

## 1.6 장고 코딩 스타일
### [장고 코딩 스타일](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)

### URL 패턴 이름에는 대시(-) 대신 밑줄(_)을 이용한다.
``` python
# 이 패턴 보단
patterns = [
    url(regex='^add-topping/$',
        view=views.add_topping,
        name='add-topping'),
]
#이 패턴을 활용하자!
patterns = [
    url(regex='^add-topping/$',
        view=views.add_topping,
        name='add_topping')
]
```

### 탬플릿 블록 이름에 대시 대신 밑줄을 이용한다.
``` html
<div id="content">
    {% block main_content %}
    content of base.html!
    {% endblock %}
</div>
```

## 1.7 자바스크립트, HTML, CSS 스타일 선택하기
### 자바스크립트 스타일 가이드
- 자바스크립트는 공식 가이드는 없고 비공식 스타일 가이드를 이용
- idiomatic.js
- Pragmatic.js
- Airbnb 자바 스크립트 스타일 가이드
- Node.js 스타일 가이드
- Code Conventions for the JavaScript Programming Language

### HTML과 CSS 스타일 가이드
- [@mdo가 쓴 코드 가이드](http://codeguide.co)
- [idomatic-css](https://github.com/necolas/idiomatic-css)

## 1.8 통합 개발 환경이나 텍스트 편집기에 종속되는 스타일의 코딩은 지양한다
