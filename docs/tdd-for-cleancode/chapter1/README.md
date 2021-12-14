#### [GO TO BACK](../README.md)

# 1. 기능 테스트를 이용한 Django 설치

### 시작전 준비
- 윈도우 스토어에서 파이썬을 설치하거나....
- git 설치 (Run Git and included Unix tools from the Windows command prompt 체크)
- Git Bash 사용 가능
- 파이썬 설치 후 symlink 생성하여 파이썬3 실행가능하게 한다.
``` shell
ln -s /c/Python34/python.exe /bin/python3.exe
```
- 파이썬이 설치 되었다면 Django 설치
``` shell
sudo pip3 install --upgrade pip
sudo pip3 install django=={최신버전}

# 설치 확인
django-admin --version

# 명령어 실행 안될시에
ln -s /C/Users/wjdan/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/Scripts/django-admin.exe /c/Users/wjdan/AppData/Local/Microsoft/WindowsApps/django-admin.exe
```

- 셀레늄 설치
``` shell
sudo pip3 install --upgrade selenium
```

### 첫 테스트 코드 작성
[테스트 코드](./functional_test.py)

### Django 가동 및 실행
``` shell
$ django-admin.py startproject superlists
$ cd uperlists
$ python3 manage.py runserver
```
