#### [GO TO BACK](../README.md)

# 2. 최적화된 장고 환경 꾸미기
## 2.1 같은 데이터 베이스를 이용하라
: 개발과 운영환경 시점에서의 이야기

### 운영 데이터를 완전히 똑같이 로컬에서 구동할 수는 없다
### 다른 종류의 데이터베이스 사이에는 다른 성격의 필드 타입과 제약 조건이 존재한다
- 물론 ORM이 어느정도 커버는 해줄 것이다.
- 하지만 제약조건 에러 constraint error는 발생할 수 있다.
### 픽스처(fixture)는 마법을 부리지 않는다.
- fixture는 단순히 하드 코딩된 간단한 데이터 세트를 생성하는 데는 좋은 도구
- 하지만 fixture는 그런 목적으로 만들어 진건 아니다. 목적을 잘 알고 사용하자.

## 2.2 pip와 virtualenv 이용하기
- pip  
: 파이썬 패키지 인덱스(Python Package Index)에서 채키지를 가져오는 도구
- virtualenv  
: 파이썬 패키지 의존성을 유지할 수 있게 독립된 파이썬 환경을 제공하는 도구
> 추천  
> virtualenvwrapper, virtualenvwrapper-win
``` shell
$ source ~/.virtualenvs/twoscoops/bin/active
$ workon twoscoop
```
## 2.3 pip를 이용하여 장고와 의존 패키지 설치하기
- pip, requirements 파일 이용
> PYTHONPATH 설정하기  
> [참고1](http://hope.simons-rock.edu/~pshields/cs/python/pythonpath.html)  
> [참고2](https://docs.djangoproject.com/en/4.0/ref/django-admin/)  

## 2.4 버전 컨트롤 시스템 이용하기
- GIT, Bitbucket, Mercurial

## 2.5 선택사항: 동일한 환경 구성
- 베이그런트 (Vagrant)
- 버츄얼박스 (VirtualBox)
- 도커 컨테이너 (Docker Container)