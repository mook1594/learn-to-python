#### [GO TO BACK](../README.md)

# 3. 어떻게 장고 프로젝트를 구성할 것인가?
- 프로젝트 레이아웃을 어떻게 꾸밀것인가?
## 3.1 장고의 기본 프로젝트 구성
- 장고 프로젝트 생성
``` shell
$ django-admin startproject {proeject 명}
$ cd {project 명}
$ django-admin startapp {app 명}
```

## 3.2 프로젝트 구성
```
<repository_root>
    <django_project_root>
        <configuration_root>
```
### 최상위 레벨: 저장소 루트
- <django_project_root>
- README.rst
- docs: 문서 관련 파일
- .gitignore
- requirements.txt
- DockerFile: 배포 관련 파일

### 두 번째 레벨: 프로젝트 루트
- 모든 python 코드는 프로젝트 루트 레벨 아래로 생성
- <configuration_root> (config)
- [manage.py](../chapter5/README.md)
- media: 개발용 사진, 미디어 파일이 올라가는 공간
- products: 기능에 대한 앱 폴더
- profiles: 기능에 대한 앱 폴더
- ratings: 기능에 대한 앱 폴더
- static: CSS, JS, 이미지 등 정적 파일 저장 장소
- templates: 시스템 통합 템플릿 파일 저장 장소

### 세 번째 레벨: 설정 루트
- settings.py
- urls.py
- wsgi.py
- asgi.py

## 3.4 virtualenv 설정
- env 관리 공간
``` shell
# mac
~/.envs/{env 명}/
# windows
c:\envs\{env 명}\

# virtualenvwrapper, virtualenvwrapper-win을 사용하면
~/.virtualenvs/{env 명}/
```
### 의존성 확인
- 지금 이용중인 virtualenv 환경에서 어떤 버전의 라이브라리를 쓰는지 알아보려면
``` shell
$ pip freeze --local
```
