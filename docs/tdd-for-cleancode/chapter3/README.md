#### [GO TO BACK](../README.md)

# 단위 테스트를 이용한 간단한 홈페이지 테스트

## 첫 Django 애플리케이션과 첫 단위 테스트
- 장고 앱 구조 생성
``` shell
$ cd superlists
$ python3 manage.py startapp lists
```

## 단위 테스트는 무엇이고, 기능 테스트와 어떤 차이가 있을까?
- 기능테스트  
: 사용자 관점에서 애플리케이션 외부를 테스트 하는 것
- 단위 테스트  
: 프로그래머 관점에서 내부를 테스트

## Django에서의 단위 테스트
- [[테스트 코드 작성(SmokeTest)]](./superlists/lists/tests.py)
- 테스트 실행
``` shell
$ python3 manage.py test
```

## Django의 MVC, URL, 뷰 함수
### 테스트 해볼것
- URL의 사이트 루트를 호출했을때, 뷰에 매칭되는지?
- 뷰가 매칭되어 응답으로 HTML을 반환하는지?
- [[test 코드 작성(HomePageTest.test_root_url_resolves_to_home_page_view)]](./superlists/lists/tests.py)
- view import 에러 확인

### 애플리케이션 코드 작성
- view 코드 작성
``` python
def home_page():
    pass
```
- 404 에러 확인
- [[url 코드 작성]](./superlists/superlists/urls.py)

## 뷰를 위한 단위 테스트
- [[test 코드 작성(HomePageTest.test_home_page_returns_correct_html)]](./superlists/lists/tests.py)
- 테스트 실패 확인 `home_page() takes 0 positional arguments but 1 was given`
- [[view 코드 작성]](./superlists/lists/views.py)

## 기억해두면 좋은 명령어 및 개념
> python3 manage.py runserver  
> python3 manage.py test