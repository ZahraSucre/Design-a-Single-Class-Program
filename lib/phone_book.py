import re

class PhoneBook():
    def __init__(self):
        self._numbers = []

    def extract_numbers(self, diary_entry):
        numbers = re.findall(r'[0-9]+', diary_entry)
        self._numbers += numbers

    def list_numbers(self):
        return self._numbers
    