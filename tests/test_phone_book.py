from lib.phone_book import PhoneBook

"""
Initially, there are no phone numbers
"""
def test_initially_has_no_numbers():
    phone_book = PhoneBook()
    assert phone_book.list_numbers() == []


"""
When we add a diary entry with no phone number in it
There are no phone numbers reflecting in the list
"""
def test_adds_entry_with_no_numbers():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My friend's number is not relevant here.")
    assert phone_book.list_numbers() == []


"""
When we add a diary entry with a phone number in it
The phone number is reflected in the list
"""
def test_extracts_numbers_from_single_entry():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My friend's number is 07900000000.")
    assert phone_book.list_numbers() == ["07900000000"]


"""
When we add three diary entries with phone numbers in them
We see all phone numbers reflected in the list
"""
def test_extracts_numbers_from_multiple_entries():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Sara's number is 07900000003" )
    phone_book.extract_numbers("Geoff's number is 07900000001" )
    phone_book.extract_numbers("Alex's number is 07900000002")
    assert phone_book.list_numbers() == ["07900000003", "07900000001", "07900000002"]


"""
When we add an entry with multiple numbers in it
We see all phone numbers reflected in the list
"""
def test_extracts_multiple_numbers_from_single_entry():
    phone_book = PhoneBook()
    phone_book.extract_numbers ("Sara's number is 07900000000 and Geoff's number is 07900000001")
    assert phone_book.list_numbers() == ["07900000000", "07900000001"]