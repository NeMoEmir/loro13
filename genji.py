class Contact:
    all_contacts = []
    def __init__(self, name, last_name, phone_number):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number

    def add_contact(self,item):
        Contact.all_contacts.append(item)

    def repr(self):
        return f'{self.name}, - {self.last_name}, - {self.phone_number}'

class Friend(Contact):
    def init(self, name):
        self.name = name

    def play_football_with_me(self):
        print(f'Пошли катать мяч {self.name}')

class ContactList(list):
    def search_by_name(self,name):
        items = Contact.all_contacts
        res = [[x] for x in items if name in x.name]
        print(res)


s = Contact('Chelovek', 'Zjivoi')
s.add_contact(s)
print(Contact.all_contacts)
v = ContactList()
v.search_by_name('Chelovek')
c = Friend('Chelovek')