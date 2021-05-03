import pytest

@pytest.mark.parametrize("foo,bar", [
    (1, 1),
    (2, 2),
    (3, 3),
])
def test_true(foo, bar):
    assert foo == bar

class TestNumbers:
    @pytest.mark.qwer
    def test_int_float(self):
        assert 1 == 1.0

    @pytest.mark.skip("broken")
    def test_int_str(self):
        assert 1 == "1"


def setup_module(module):
    print("setting up MODULE {0}".format(module.__name__))

def teardown_module(module):
    print("tearing down MODULE {0}".format(module.__name__))

def test_a_function():
    print("RUNNING TEST FUNCTION")

class BaseTest:

    def setup_class(cls):
        print("setting up CLASS {0}". format(cls.__name__))

    def teardown_class(cls):
        print("tearing down CLASS {0}\n".format(cls.__name__))

    def setup_method(self, method):
        print("setting up METHOD {0}".format(method.__name__))

    def teardown_method(self, method):
        print("tearing down METHOD {0}".format(
            method.__name__
        ))

class TestClass1(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 1-1")

    def test_method_2(self):
        print("RUNNING METHOD 1-2")

class TestClass2(BaseTest):
    def test_method_1(self):
        print("RUNNING METHOD 2-1")

    def test_method_2(self):
        print("RUNNING METHOD 2-2")
