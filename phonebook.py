import os


class PhoneBook:
    def __init__(self, cache_directory):
        self.records = {}
        self.filename = os.path.join(cache_directory, "phonebook.txt")
        self.cache = open(self.filename, "w")

    def add(self, name, number):
        self.records[name] = number

    def lookup(self, name):
        return self.records[name]

    def names(self):
        return self.records.keys()

    def clear(self):
        self.cache.close()
        os.remove(self.filename)
