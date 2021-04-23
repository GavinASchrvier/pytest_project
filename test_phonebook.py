from phonebook import PhoneBook


def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Bob", "12345")
    assert "1234567" == phonebook.lookup("Bob")
