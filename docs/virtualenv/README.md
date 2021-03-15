#### [GO TO BACK](../README.md)

# Virtual Env

## Pyenv

### pyenv 설치
```shell
$ brew update
$ brew install pyenv
```

### 설치 가능한 python 목록확인
```shell
$ pyenv install -list
```

### 파이선 설치
```shell
$ pyenv install <파이썬 버전>
$ pyenv uninstall <파이썬 버전>
```

### 설치한 파이선 목록
```shell
$ pyenv versions
```

### 파이썬 글로벌 버전 설정
```shell
$ pyenv global <파이썬 버전>
```

## pyenv-virtualenv
### pyenv-virtualenv 설치
```shell
$ brew install pyenv-virtualenv
```

### 가상 환경 생성
```shell
$ pyenv virtualenv <version> <가상환경 이름>
$ pyenv virtualenv <가상 환경 이름>
```

### 가상 환경 삭제
```shell
$ pyenv uninstall <가상 환경 이름>
```

### 가상 환경 실행
```shell
$ pyenv activate <가상환경 이름>
$ pyenv deactive <가상환경 이름>
```

## 환경 변수 설정
```shell
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
$ source ~/.bash_profile
```