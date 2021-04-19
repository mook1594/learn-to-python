class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

c1 = Contact("John A", "johna@ex.net")
c1 = Contact("John B", "johnb@ex.net")
c1 = Contact("John C", "johnc@ex.net")
search = [c.name for c in Contact.all_contacts.search('John')]
print(search)
