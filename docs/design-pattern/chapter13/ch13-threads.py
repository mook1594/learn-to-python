from threading import Thread

import json
from urllib.request import urlopen
import time

CITIES = [
    "Edmonton", "Victoria", "Winnipeg", "Fredericton",
    "St.John'", "Halifax", "Toronto", "Charlottetown",
    "Quebec City", "Regina"
]

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        url_template = ('http://api.openweathermap.org/data/2.5/weather?q={},CA&units=metric')
        response = urlopen(url_template.format(self.city))
        data = json.loads(response.read().decode())
        self.temperature = data['main']['temp']

threads = [TempGetter(c) for c in CITIES]

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for thread in threads:
    print("it is {0.temperature:.0f}°C in {0.city}".format(thread))

print("Got {} temps in {} seconds".format(len(threads), time.time() - start))

class InputReader(Thread):
    def run(self):
        self.line_of_text = input()

print("Enter some text and press enter: ")
thread = InputReader()
thread.start()

count = result = 1
while thread.is_alive():
    result = count * count
    count += 1

print("calculated squares up to {0} * {0} = {1}".format(count, result))
print("while you typed '{}'".format(thread.line_of_text))
