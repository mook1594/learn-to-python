class Color:
    def __init__(self, rgb_value, name):
        self._rgb_value = rgb_value
        self._name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    def _del_name(self):
        del self._name

    name = property(_get_name, _set_name, _del_name, 'name property')

c = Color("#ff0000", "bright red")
c.name = 'dddd'
print(c.name)
c._name = 'red'
print(c.name)
del c.name
