#### [GO TO BACK](../README.md)

# unittest 모듈을 이용한 기능 테스트 확장
## 기능 테스트를 이용한 최소 기능의 애플리케이션 설계
- 기능 테스트(functional test) == 승인 테스트(acceptance test) == 종단간 테스트(end-to-end test)  
: 외부 사용자 관점에 서의 테스트
``` python
browser = webdriver.Chrome()
# 유저가 해당 웹사이트를 접속
browser.get('http://localhost:8000')

# 웹 페이지 타이틀과 헤더가 To-Do로 표시하고 있음
assert 'To-Do' in browser.title

# 해당 사이트를 이용한다

# 어쩌구 저쩌구 버튼을 클릭해서 어쩌구 저쩌구 해서
# 이렇궁 저렇궁 되면
# 요롷게 저렇게 한다

# 사용이 끝나면 브라우저를 종료한다
browser.quit()
```

## 파이썬 기본 라이브러리의 unittest
 [[테스트 코드 작성]](./functional_test.py)
 - `browser.implicitly_wait(3)` 암묵적인 대기 (초 단위)

 ### 유용한 TDD 개념
 - 사용자 스토리 (User story)
 - 예측된 실패 (Expected failure)