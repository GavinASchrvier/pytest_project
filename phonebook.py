class PhoneBook:
    def __init__(self):
        self.records = {}

    def add(self, name, number):
        self.records[name] = number

    def lookup(self, name):
        return self.records[name]