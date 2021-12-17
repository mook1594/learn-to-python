#### [GO TO BACK](../README.md)

# 4. 장고 앱 디자인의 기본
- 장고 프로젝트: 장고 웹 프레임워크를 기반으로 한 웹 애플리케이션
- 장고 앱: 프로젝트 한 기능을 표현하기 위해 디자인된 작은 라이브러리
- INSTALLED_APPS: 프로젝트에서 이용하려는 앱을 설정
- [서드 파티 장고 패키지](../chapter21/README.md): 패키지화된 재사용 가능한 플러그인

## 4.1 장고 앱 디자인 황금률
- 한 번에 한 가지 일을 하고 그 한 가지 일을 매우 충실히 하는 프로그램을 짜는 것이다.
### 실제 예를 통해 본 앱
> 아이스크림 상점을 위한 앱 개발
- flavors app: 상점 모든 아이스크림 종류가 기록되고 그 목록을 보여주는 앱
- blog app: 상점의 공식 블로그
- events app: 행사 내용을 상점 웹 사이트에 보여주는 앱
- shop app: 온라인 주문을 통해 아이스크림을 판매하는 앱
- ticket app: 무제한 아이스크림 행사에 이용될 티켓 판매를 관리하는 앱

## 4.2 장고 앱 이름 정하기
- 앱 이름은 가능한 한 단어로 된 이름을 이용
- 앱 이름은 PEP-8 규약에 따라 소문자로 구성된 숫자, 필요하다면 _ 사용
- -, ., 공백이나 특수문자를 포함하지 않음

## 4.3 확신 없이는 앱을 확장하지 않는다
- 앱을 디자인 하는데 처음부터 완벽하게 하려고 고민하지 말자
- 하지만 작은 앱 여러개를 구성함을 인지해야할것

## 4.4 앱 안에는 어떤 모듈이 위치하는가
### 공통 앱 모듈
- admin.py
- forms.py
- management
- migration
- models.py
- templatetags
- tests
- urls.py
- views.py

### 비 공통 앱 모듈
- behaviors.py : 모델 믹스인 위치
- constants.py : 세팅을 저장하는 장소의 이름
- context-processors.py 
- decorators.py : 데코레이터
- exceptions
- fields.py : 폼 필드 이용에 사용
- factories.py : 테스트 데이터 팩터리 파일
- helpers.py : 헬퍼 함수, 뷰와 모델을 가볍게 하기위한 장소
- managers.py : 모델이 커질경우 커스텀 모델 메니져 구현
- middleware.py
- signals.py : 커스텀 시그널 
- utils.py : helpers와 유사한 기능
- viewmixins.py : 뷰 믹스인을 모아둠으로 뷰 모듈과 패키지를 더 가볍게 할 수 있음
