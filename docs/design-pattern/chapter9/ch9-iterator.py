class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)

class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self

iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

for i in iterable:
    print(i)

print('=' * 30)

### filter
logs = [];
logs.append("Jan 26, 2015 11:25:25  DEBUG   This is a debugging message.")
logs.append("Jan 26, 2015 11:25:36  INFO    This is an information method.")
logs.append("Jan 26, 2015 11:25:46  WARNING This is a warning. It could be serious.")
logs.append("Jan 26, 2015 11:25:52  WARNING Another warning sent.")
logs.append("Jan 26, 2015 11:25:59  INFO    Here's some information.")
logs.append("Jan 26, 2015 11:26:13  DEBUG   Debug messages are only useful if you want to figure something out.")
logs.append("Jan 26, 2015 11:26:32  INFO    Information is usually harmless, but helpful.")
logs.append("Jan 26, 2015 11:26:40  WARNING Warnings should be heeded.")
logs.append("Jan 26, 2015 11:26:54  WARNING Watch for warnings.")

print(logs)

warnings = (l for l in logs if 'WARNING' in l)
for l in warnings:
    print(l)

warnings1 = (l.replace('WARNING', '') for l in logs if 'WARNING' in l)
for l in warnings1:
    print(l)

class WarningFilter:
    def __init__(self, insequence):
        self.insequence = iter(insequence)

    def __iter__(self):
        return self

    def __next__(self):
        l = self.insequence.next()
        while l and 'WARNING' not in l:
            l = self.insequence.next()
        if not l:
            raise StopIteration
        return l.replace('WARNING', '')

filter = WarningFilter(logs)
print(filter)
for l in filter:
    print(l)
