stock = "FB", 75.00, 75.03, 74.90
stock2 = ("FB", 75.00, 75.03, 74.90)

print(stock)
print(stock2)

import datetime
def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)

mid_value, date = middle(("FB", 75.00, 75.03, 74.90),
                         datetime.date(2014, 10, 31))

stock = "FB", 75.00, 75.03, 74.90
high = stock[2]
print(high)

from collections import namedtuple
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("FB", 75.00, high=75.03, low=74.90)
print(stock.high)
symbol, current, high, low = stock
print(current)
stock.current = 74.00
