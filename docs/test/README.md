#### [GO TO BACK](../README.md)

# Test

### testing 종류
- Unit tests
- Regression tests
- Integration tests
- 이외의 일반적인 테스트의 종류는 다음과 같다. 블랙박스, 화이트 박스, 수동, 자동, 카나리아, 스모크, 적합성 평가(conformance), 인수(acceptance), 기능성, 시스템, 성능, 로드, 스트레스 테스트 등.

### 테스트 케이스 작성
#### 기본 형태
```python
class TestClass(django.test.TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass
    def tearDown(self):
        # Clean up run after every test method.
        pass
    def test_something_that_will_pass(self):
        self.assertFalse(False)
    def test_something_that_will_fail(self):
        self.assertTrue(False)
```

#### 테스트 파일
```
/tests/
    __init__.py (디렉토리가 패키지 임을 알려줌)
    test_models.py
    test_forms.py
    test_views.py
```

#### 테스트 예제
```python
from django.test import TestCase

class TestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("SetUpTestData: Run once to set up non-modified data for all class methods.")
        pass
    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)
    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)
    def test_one_plus_one_equals_two(self):
        print("Method: test_")
        self.assertEqual(1 + 1, 2)
```
- setUpTestData: 한번만 실행됨
- setUp: 테스트 메서드가 실행될때마다 각각 실행됨

### 테스트 동작 
```shell
$ python3 manage.py test
```

## Request Test
```python
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'}, format = 'json')
request = factory.post('/notes/', json.dumps({'title': 'new idea'}), content_type='application/json')

```
### Force authentication
```python
factory = APIRequestFactory()
user = User.objects.get(username='olivia')
view = AccountDetail.as_view()

# Make an authenticated request to the view...
request = factory.get('/accounts/django-superstars/')
force_authenticate(request, user=user)
response = view(request)
```
```python
user = User.objects.get(username='olivia')
request = factory.get('/accounts/django-superstars/')
force_authenticate(request, user=user, token=user.auth_token)
```