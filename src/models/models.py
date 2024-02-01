from abc import ABC, abstractmethod
import json
from datetime import date
from sql import executeQuery


class Model(ABC):
    table = None

    @classmethod
    def list(cls):
        result = executeQuery("SELECT * FROM %s ;", cls.table, "GET")
        for data in result:
            print(data)

    @classmethod
    def view(cls, id):
        result = executeQuery("SELECT * FROM %s WHERE id=%s;", (cls.table, id), "GET")

        for data in result:
            print(data)
            return data
        print(f"id not found")
        return "id not found"

    @classmethod
    def delete(cls, id):
        result = executeQuery("DELETE FROM %s WHERE id = %s", (cls.table, id), "DELETE")
        if result == 0:
            print("id not found")

    @classmethod
    def create(cls, table, data):
        lastId = executeQuery(
            "INSERT INTO %s (%s) VALUES %s;",
            (table, ",".join(list(data.keys())), tuple(data.values())),
            "POST",
        )
        print(type(lastId))
        return lastId

    @classmethod
    def update(self, table, data, id):
        setColumns = []
        for key, value in data.items():
            setColumns.append(f"{key} = '{value}'")

        executeQuery(
            "UPDATE %s SET %s WHERE id=%s", (table, ",".join(setColumns), id), "PATCH"
        )
