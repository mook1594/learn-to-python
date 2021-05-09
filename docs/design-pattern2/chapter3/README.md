#### [GO TO BACK](../README.md)

# 3. The Factory Pattern
> Building Factories to create Objects
#### Simple Factory Pattern
```python
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")

class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")

## Forest factory defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

## client code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Which animal should make_sound Dog or Cat?")
    ff.make_sound(animal)
```
#### Factory Method Pattern
```python
from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")
        
class PatentSection(Section):
    def describe(self):
        print("Patent Section")
        
class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSections(self, section):
        self.sections.append(section)

class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())

if __name__ == '__main__':
    profile_type = input("Which Profile you'd like to create? [LinkedIn or FaceBook]")
    profile = eval(profile_type.lower())()
    print("Creating Profile..", type(profile).__name__)
    print("Profile has sections --", profile.getSections())
```
#### Abstract Factory Pattern
```python
from abc import ABCMeta, abstractmethod

class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass
    @abstractmethod
    def createNonVegPizza(self):
        pass
class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()
    def createNonVegPizza(self):
        return ChickenPizza()
class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()
    def createNonVegPizza(self):
        return HamPizza()

class VegPizza(metaclass=ABCMeta): 
    @abstractmethod
    def prepare(self, VegPizza): 
        pass
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza): 
        pass
class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)

class ChickenPizza(NonVegPizza): 
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)
class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)
class HamPizza(NonVegPizza): 
    def serve(self, VegPizza):
        print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)

class PizzaStore:
    def __init__(self):
        pass
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]: 
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza() 
            self.VegPizza = self.factory.createVegPizza() 
            self.VegPizza.prepare() 
            self.NonVegPizza.serve(self.VegPizza)

pizza = pizza.makePizzas()
PizzaStore()
```
