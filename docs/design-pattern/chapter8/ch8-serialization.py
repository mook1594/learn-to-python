### Serializing Objects

import pickle

some_data = ['a list', 'containing', 5, 'values including another list', ['inner', 'list']]

with open('pickled_list', 'wb') as file:
    pickle.dump(some_data, file)

with open('pickled_list', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
assert loaded_data == some_data

from threading import Timer
import datetime
from urllib.request import urlopen

class UpdatedURL:
    def __init_(self, url):
        self.url = url
        self.contents = ''
        self.last_updated = None
        self.update()

    def update(self):
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self):
        self.timer = Timer(3600, self.update)
        self.timer.setDaemon(True)
        self.timer.start()

u = UpdatedURL('http://news.yahoo.com/')
import pickle
serialized = pickle.dumps(u)
