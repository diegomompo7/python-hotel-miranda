from src.models import Users

def test_list_users():
    assert isinstance(Users.list(), object)

def test_view_user():
    assert isinstance(Users.view(2), object)
    
def test_error_view_user():
    assert Users.view(30) == "id not found"

def test_create_user():
    assert isinstance(Users.create(), object)
    
def test_update_user():
    print("\n")
    print("Update")
    assert isinstance(Users.update(1), object)
    