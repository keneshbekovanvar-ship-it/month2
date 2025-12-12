class Contact: """Class describing a single contact."""

def __init__(self, name: str, phone_number: str):
    self.name = name

    self.phone_number = phone_number
    self.phone = phone_number

@staticmethod
def validate_phone_number(phone_number: str) -> bool:
    """Return True if phone_number contains exactly 10 digits, otherwise False."""
    if not isinstance(phone_number, str):
        return False
    return phone_number.isdigit() and len(phone_number) == 10

class ContactList: """Container for storing contacts."""

all_contacts = []

@classmethod
def add_contact(cls, name: str, phone_number: str):
    """
    Validate phone number and add a new Contact to cls.all_contacts.

    Raises:
        ValueError: if phone number is invalid
    """
    if not Contact.validate_phone_number(phone_number):
        raise ValueError(f"Invalid phone number: {phone_number}. Must contain exactly 10 digits.")

    contact = Contact(name, phone_number)
    cls.all_contacts.append(contact)
    return contact
