#### [GO TO BACK](../README.md)

# 2. The Singleton Design Pattern
#### Singleton
```python
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)
```
#### Lazy instantiation
```python
class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called")
        else:
            print("Instance already created:", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s = Singleton()
print("Object created", Singleton.getInstance())
s1 = Singleton()
```
#### Singletons And Metaclasses
```python
class MyInt(type):
    def __call__(self, *args, **kwargs):
        print("***** Here's My int *****", args)
        print("Now do whatever you want with these objects...")
        return type.__call__(self, *args, **kwargs)

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4, 5)
```
```python
class MetaSingleton(type):
    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self._instance[self]

class Logger(metaclass=MetaSingleton)
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
```
#### Singleton pattern Ex1
```python
import sqlite3
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()
```
#### Singleton pattern Ex2
```python
class HealthCheck:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance
    def __init__(self):
        self._servers = []
    def addServer(self):
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
    def changeServer(self):
        self._servers.pop()
        self._servers.append("Server 5")

hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
for i in range(4):
    print(hc1._servers[i])
hc2.changeServer()
for i in range(4):
    print(hc2._servers[i])
```
