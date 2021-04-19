import abc

class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

    @classmethod
    def __subclasscheck__(cls, subclass):
        if cls is MediaLoader:
            # 클래스 계층 구조의 모든 부모 클래스를 포함하여 클래스에있는 메서드 및 속성 집합을 가져 오는 것입니다.
            attrs = set(dir(subclass))
            # 오버라이딩 했는지 확인 체크
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented

class Wav(MediaLoader):
    pass
x = Wav()

class Ogg(MediaLoader):
    ext = '.ogg'
    def play(self):
        pass
o = Ogg()
