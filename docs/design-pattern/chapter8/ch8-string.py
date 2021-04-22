### String manipulation
a = 'hello'
b = 'world'
c = '''a multiple 
line string'''
d = """More
multiple"""
e = ('Three ' + 'Strings' +
     "together'")

print ('=' * 30)

print(float('45\u06602'))
s = 'hello world'
print(s.count('l'))
print(s.find('l'))
print(s.rindex('e'))
print(s.split(' '))
print('#'.join(s.split(' ')))
print(s.partition(' '))

print ('=' * 30)

### String Formatting
template = "Hello {}, you are currently {}."
print(template.format('Dusty', 'writing'))
template = "Hello {0}, you are {1}. Your name is {0}."
print(template.format('Dusty', 'writing'))

print ('=' * 30)

### Escaping braces
template = """ public class {0} {{
    public static void main(String[] args) {{ System.out.println("{1}");
}} }}"""
print(template.format("MyClass", "print('hello world')"));

print ('=' * 30)

### Keyword arguments
template = """
From: <{from_email}> 
To: <{to_email}> Subject: {subject}
{message}"""

print(template.format(
    from_email="a@example.com",
    to_email="b@example.com",
    message="Here's some mail for you. " " Hope you enjoy the message!",
    subject="You have mail!"
))

print("{} {label} {}".format("x", "y", label="z"))

print ('=' * 30)

### Container lookups
emails = ("a@example.com", "b@example.com")
message = {'subject': "You Have Mail!", 'message': "Here's some mail for you!" }
template = """
From: <{0[0]}>
To: <{0[1]}>
Subject: {message[subject]} {message[message]}"""

print(template.format(emails, message=message))

emails = ("a@example.com", "b@example.com")
message = {
    'emails': emails,
    'subject': "You Have Mail!",
    'message': "Here's some mail for you!"
}
template = """
From: <{0[emails][0]}>
To: <{0[emails][1]}>
Subject: {0[subject]} {0[message]}"""

print(template.format(message))
print ('=' * 30)
### Object lookups
class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message

email=EMail("a@example.com", "b@example.com", "You Have Mail!",
  "Here's some mail for you!")
template = """
From: <{0.from_addr}> 
To: <{0.to_addr}> 
Subject: {0.subject} {0.message}"""

print(template.format(email))
print ('=' * 30)

### Making it look right
subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax
print("Sub: ${0} Tax: ${1} Total: ${total}".format(subtotal, tax, total=total))
print("Sub: ${0:0.2f} Tax: ${1:0.2f} " "Total: ${total:0.2f}".format(subtotal, tax, total=total))
print('=' * 30)

orders = [('burger', 2, 5), ('fries', 3.5, 1), ('cola', 1.75, 3)]
print("PRODUCT QUANTITY PRICE SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
print("{0:10s}{1: ^9d} ${2: <8.2f}${3: >7.2f}".format(product, quantity, price, subtotal))
print('=' * 30)
import datetime
print("{0:%Y-%m-%d %I:%M%p }".format(datetime.datetime.now()))
print('=' * 30)
### Matching patterns
import re
search_string = 'hello world'
pattern = 'hello world'

match = re.match(pattern, search_string)

if match:
    print('regex matches')

pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
search_string = "some.user@example.com"
match = re.match(pattern, search_string)
if match:
    domain = match.groups()[0]
print(domain)
print('=' * 30)
