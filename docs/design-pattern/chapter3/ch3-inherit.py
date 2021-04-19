class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("{} - {}".format(order, self.name))

c = Contact("Some Body", "somebody@example.net")
s = Supplier("Suppiler", "supplier@example.net")
print(c.name, c.email, s.name, s.email)
print(c.all_contacts)
