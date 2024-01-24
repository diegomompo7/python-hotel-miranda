from abc import ABC, abstractmethod
import json


class Model(ABC):
    json_path = None

    @classmethod
    def list(cls):
        if cls.json_path is not None:
            with open(cls.json_path, "r") as file:
                data = json.load(file)
                print(f"Listening {cls.__name__}")
                print(data)
                return data
        else:
            print(f"Error: JSON path for {cls.__name__}")

    @classmethod
    def view(cls, id):
        checkView = False
        if cls.json_path is not None:
            with open(cls.json_path, "r") as file:
                data = json.load(file)
                for book in data:
                    if int(id) == book.get("id"):
                        print(f"View {id}")
                        print(book)
                        return book
                
                if checkView == False:
                    print("id not found")
                    return "id not found"

        else:
            print(f"Error: JSON path for {cls.__name__}")

    @classmethod
    def delete(cls, id):
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass
