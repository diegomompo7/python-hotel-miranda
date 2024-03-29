from src.models import Bookings

def test_list_bookings():
    assert isinstance(Bookings.list(), object)

def test_view_booking():
    print("\n")
    assert  isinstance(Bookings.view(2), object)
    
def test_error_view_booking():
    print("\n")
    assert Bookings.view(30) == "id not found"

def test_create_booking():
    print("\n")
    print("Create")
    assert isinstance(Bookings.create(), object)
    
def test_update_booking():
    print("\n")
    print("Update")
    assert isinstance(Bookings.update(1), object)
    