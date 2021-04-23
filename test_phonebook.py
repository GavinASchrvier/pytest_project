import pytest

from phonebook import PhoneBook


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "12345")
    assert "12345" == phonebook.lookup("Bob")


@pytest.fixture()
def phonebook():
    return PhoneBook()


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1343")
    phonebook.add("Susy", "13432")
    names = phonebook.names()
    assert "Bob", "Susy" in names


def test_name_not_found(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")

