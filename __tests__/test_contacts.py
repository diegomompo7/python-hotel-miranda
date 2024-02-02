from src.models import Contacts

def test_list_contacts():
    assert isinstance(Contacts.list(), object)

def test_view_contact():
    print("\n")
    assert isinstance(Contacts.view(2), object)
    
def test_error_view_contact():
    print("\n")
    assert Contacts.view(30) == "id not found"

def test_create_contact():
    print("\n")
    print("Create")
    assert isinstance(Contacts.create(), object)
    
def test_update_contact():
    print("\n")
    print("Update")
    assert isinstance(Contacts.update(1), object)
    