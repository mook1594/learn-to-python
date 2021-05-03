#### [GO TO BACK](../README.md)

# 12. Testing Object-oriented Programs

### Unittest
#### [샘플 코드](./ch12-unittest.py)

### Assert Methods
- assertGreater
- assertGreaterEqual
- assertLess
- assertLessEqual
- assertIn
- assertNotIn
- assertIsNone
- assertIsNotNone
- assertSameElements
- assertSequenceEqualassertDictEqual
- assertSetEqual
- assertSetEqual
- assertListEqual
- assertTupleEqual

### Ignoring broken tests
- expectedFailure()
- skip(reason)
- skipIf(condition, reason)
- skipUnless(condition, reason)

```python
import unittest


class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(False, True)

    @uniitest.skipIf(sys.version_info.minor == 4, "broken on 3.4")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(sys.platform.startswith('linux'), "broken unless on linux")
    def test_skipunless(self):
        self.assertEqual(False, True)
```

### Pytest
#### [샘플 코드](./ch12-pytest.py)

### Setup Variables
```python
from stats import StatsList

def pytest_funcarg__valid_stats(request):
    return StatsList([1,2,2,3,3,4])

def test_mean(valid_stats):
    assert valid_stats.mean() == 2.5
    
def test_median(valid_stats):
    assert valid_stats.median() == 2.5 valid_stats.append(4)
    assert valid_stats.median() == 3
    
def test_mode(valid_stats):
    assert valid_stats.mode() == [2,3] valid_stats.remove(2)
    assert valid_stats.mode() == [3]
```
```python
import tempfile 
import shutil 
import os.path

def pytest_funcarg__temp_dir(request): 
    dir = tempfile.mkdtemp() 
    print(dir)

    def cleanup(): 
        shutil.rmtree(dir)
    request.addfinalizer(cleanup)

    return dir
def test_osfiles(temp_dir): 
    os.mkdir(os.path.join(temp_dir, 'a')) 
    os.mkdir(os.path.join(temp_dir, 'b')) 
    dir_contents = os.listdir(temp_dir) 
    assert len(dir_contents) == 2
    assert 'a' in dir_contents
    assert 'b' in dir_contents
```
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind(('localhost',1028))
s.listen(1)

    while True:
        client, address = s.accept() 
        data = client.recv(1024) 
        client.send(data) 
        client.close()
```
```python
import subprocess
import socket
import time

def pytest_funcarg__echoserver(request):
    def setup():
        p = subprocess.Popen(
            ['python3', 'echo_server.py'])
        time.sleep(1) 
        return p

    def cleanup(p): 
        p.terminate()
        
    return request.cached_setup( 
        setup=setup,
        teardown=cleanup, 
        scope="session")

def pytest_funcarg__clientsocket(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect(('localhost', 1028)) 
    request.addfinalizer(lambda: s.close())
    return s

def test_echo(echoserver, clientsocket): 
    clientsocket.send(b"abc")
    assert clientsocket.recv(3) == b'abc'
    
def test_echo2(echoserver, clientsocket): 
    clientsocket.send(b"def")
    assert clientsocket.recv(3) == b'def'

```

### Mock
#### [샘플 코드](./ch12-mock.py)

### Test Coverage
```shell
$ pip install coverage
$ coverage run {python file}
$ coverage report
```
```shell
Name                      Stmts     Exec    Cover 
-------------------------------------------------- 
coverage_unittest             7         7     100% 
stats                        19         6      31% 
-------------------------------------------------- 
TOTAL                        26        13      50%

Missing 
----------- 
8-12, 15-23
```
```shell
$ pip install pytest-coverage
```
