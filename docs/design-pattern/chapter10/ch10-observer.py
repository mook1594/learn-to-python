class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product
    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()

class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self, *args, **kwargs):
        print(self.inventory.product)
        print(self.inventory.quantity)

i = Inventory()
c = ConsoleObserver(i)
i.attach(c)
i.product = 'Widget'
i.quantity = 5
i2 = Inventory()
c1 = ConsoleObserver(i2)
c2 = ConsoleObserver(i2)
i2.attach(c1)
i2.attach(c2)
i.product = 'Gadget'
