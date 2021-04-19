def funny_division(divider):
    try:
        return 100 / divider
    except ZeroDivisionError:
        return "Zero is not a good idea!"
    except TypeError:
        return "Only Integer"

print(funny_division(0))
print(funny_division(50))
print(funny_division(50.0))
print(funny_division("hello"))

class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesnt have ${}".format(amount))
        self.amount = amount
        self.balance = balance
    def overage(self):
        return self.amount - self.balance

try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print("what ? ${}".format(e.overage()))
