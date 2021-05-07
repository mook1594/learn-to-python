#### [GO TO BACK](../README.md)

# 1. Introduction to Design Patterns
#### Methods
```python
class Person(object):
    def __init__(self, name, age): # constructor
        self.name = name # data members / attributes
        self.age = age

    def get_person(self,): # member function
        return "<Person (%s, %s)>" % (self.name, self.age)

    p = Person("John", 32) # p is an object of type Person
    print("Type of Object:", type(p), "Memory Address:", id(p))
```
#### Polymorphism
```python
a = "John"
b = (1,2,3)
c = [3,4,6,7,8]
print(a[1], b[0], c[2])
```
#### Inheritance
```python
class B:
    class A:
        def a1(self):
            print("a1")
    class B(A):
        def b(self):
            print("b")
b = B()
b.a1()
```
#### Abstraction
```python
class Adder:
    def __init__(self):
        self.sum = 0
    def add(self, value):
        self.sum += value

acc = Adder()
for i in range(99):
    acc.add(i)

print(acc.sum)
```
#### Composition
```python
class A(object):
    def a1(self):
        print("a1")
class B(object):
    def b(self):
        print("b")
        A().a1()

objectB = B()
objectB.b()
```
