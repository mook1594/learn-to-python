#### [GO TO BACK](../README.md)

# 4. When to Use Object-oriented Programming

### Properties
- [코드](./ch5-class-properties.py)

### Decorators - properties
```python
class Foo:
    @property
    def foo(self):
        return self._foo
    
    @foo.setter
    def foo(self, value):
        self._foo = value
        
    @foo.deleter
    def foo(self):
        del self._foo

```

### Case Study
- [코드](./ch5-study-case.py)
