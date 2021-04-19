class PhoneBook:
    def __init__(self):
        self.records = {}

    def add(self, name, number):
        self.records[name] = number

    def lookup(self, name):
        return self.records[name]


def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Bob", "12345")
    assert "1234567" == phonebook.lookup("Bob")
