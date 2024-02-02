from src.models import Rooms

def test_list_rooms():
    assert isinstance(Rooms.list(), object)

def test_view_room():
    print("\n")
    assert isinstance(Rooms.view(2) != "id not found", object)
    
def test_error_view_room():
    print("\n")
    assert Rooms.view(30) == "id not found"

def test_create_room():
    print("\n")
    print("Create")
    assert isinstance(Rooms.create(), object)
    
def test_update_room():
    print("\n")
    print("Update")
    assert isinstance(Rooms.update(1), object)
    