#### [GO TO BACK](../README.md)

# 4. Expecting the Unexpected

### 에러 발생
```python
class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")\
        super().append(integer)
```

### try-catch
```python
try:
    no_return()
except:
    print("I caught and exception")

```

### [Exception](./ch4-exception.py)
