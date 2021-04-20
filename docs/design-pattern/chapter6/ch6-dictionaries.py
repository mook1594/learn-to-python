stocks = {
    'GOOG': (613.30, 625.86, 610.50),
    'MSFT': (30,25, 30.70, 30.19)
}

print(stocks['GOOG'])
print(stocks.get('RIM', 'NOT FOUND'))
print(stocks.setdefault('GOOG', 'INVALID'))
print(stocks.setdefault('BBRY', (10.50, 10.62, 10.39)))
print(stocks['BBRY'])
for stock, values in stocks.items():
    print("{} last value is {}".format(stock, values[0]))

random_keys = {}
random_keys['astring'] = 'somestring'
random_keys[5] = 'aninteger'
random_keys[25.2] = 'floats work too'
random_keys[('abc', 123)] = 'so do tuples'

def letter_frequency(sentence):
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies

from collections import defaultdict, Counter

## defaultdict
def letter_frequency(sentence):
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

num_items = 0
def tuple_counter():
    global num_items
    num_items += 1
    return (num_items, [])

d = defaultdict(tuple_counter)
d['a'][1].append('hello')
d['b'][1].append('world')
print(d)


## Counter
responses = [
    "vanilla",
    "chocolate", "vanilla", "vanilla", "caramel", "strawberry", "vanilla"
]
print(Counter(responses).most_common(3))
print(
    "The children voted for {} ice cream".format(
        Counter(responses).most_common(1)[0][0]
    )
)


## Lists
import string
CHARACTERS = list(string.ascii_letters) + ['']

def letter_frequency(sentence):
    frequency = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequency[index] = (letter, frequency[index][1] + 1)
    return frequency

print(letter_frequency('slgkjownobaijsdfo'))

## Sorting lists
class WeirdSortee:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, other):
        if self.sort_num:
            return self.number < other.number
        return self.string < other.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)

a = WeirdSortee('a', 4, True)
b = WeirdSortee('b', 3, True)
c = WeirdSortee('c', 2, True)
d = WeirdSortee('d', 1, True)
l = [a,b,c,d]
print(l)
l.sort()
print(l)

from functools import total_ordering

@total_ordering
class WeirdSortee2:
    def __init__(self, string, number, sort_num):
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, other):
        if self.sort_num:
            return self.number < other.number
        return self.string < other.string

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)

    def __eq__(self, other):
        return all((
            self.string == other.string,
            self.number == other.number,
            self.sort_num == other.sort_num
        ))

## Sets
song_library = [('Phantom Of The Opera', 'Sarah Brightman'),
                 ("Knocking On Heaven's Door", "Guns N' Roses"),
                 ("Captain Nemo", "Sarah Brightman"),
                 ("Pattern In The Ivy", "Opeth"),
                 ("November Rain", "Guns N' Roses"),
                 ("Beautiful", "Sarah Brightman"),
                 ("Mal's Song", "Vixy and Tony")]
artists = set()
for song, artist in song_library:
    artists.add(artist)

print(artists)
print("Opeth" in artists)
for artist in artists:
    print("{} play good music".format(artist))
alphabetical = list(artists)
alphabetical.sort()
print(alphabetical)
print("="*40)
my_artists = {"Sarah Brightman", "Guns N' Roses", "Opeth", "Vixy and Tony"}
auburns_artists = {"Nickelback", "Guns N' Roses", "Savage Garden"}
print("All: {}".format(my_artists.union(auburns_artists)))
print("Both: {}".format(auburns_artists.intersection(my_artists)))
print("Either but not both: {}".format(my_artists.symmetric_difference(auburns_artists)))
print("="*40)

my_artists = {"Sarah Brightman", "Guns N' Roses", "Opeth", "Vixy and Tony"}
bands = {"Guns N' Roses", "Opeth"}
print("my_artists is to bands:")
print("issuperset: {}".format(my_artists.issuperset(bands)))
print("issubset: {}".format(my_artists.issubset(bands)))
print("difference: {}".format(my_artists.difference(bands)))
print("*"*40)
print("bands is to my_artists:")
print("issuperset: {}".format(bands.issuperset(my_artists)))
print("issubset: {}".format(bands.issubset(my_artists)))
print("difference: {}".format(bands.difference(my_artists)))


from collections import KeysView, ItemsView, ValuesView

class DictSorted(dict):
    def __new__(*args, **kwargs):
        new_dict = dict.__new__(*args, **kwargs)
        new_dict.ordered_keys = []
        return new_dict

    def __setitem__(self, key, value):
        '''self[key] = value syntax'''
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        super().__setitem__(key, value)

    def setdefault(self, key, value):
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        return super().setdefault(key, value)

    def keys(self):
        return KeysView(self)

    def values(self):
        return ValuesView(self)

    def items(self):
        return ItemsView(self)

    def __iter__(self):
        '''for x in self syntax'''
        return self.ordered_keys.__iter__()

ds = DictSorted()
d = {}
ds['a'] = 1
ds['b'] = 2
ds.setdefault('c', 3)
d['a'] = 1
d['b'] = 2
d.setdefault('c', 3)
for k,v in ds.items():
    print(k,v)
