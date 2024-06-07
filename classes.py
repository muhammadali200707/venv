from db.manage import Database


class Country:
    table_name = "country"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = f"SELECT * FROM {Country.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO country(name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data, table) -> str:
        if column == "id":
            query = f"UPDATE {table} SET {column} = {new_data} WHERE {column} = {old_data}"
        else:
            query = f"UPDATE {table} SET {column} = '{new_data}' WHERE {column} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data, table):
        query = f"DELETE FROM {table} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class City(Country):
    table_name = "city"

    def __init__(self, name, country_id):
        Country.__init__(self, name)
        self.country_id = country_id

    @staticmethod
    def select():
        query = f"SELECT * FROM {City.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO city(name, country_id) VALUES('{self.name}', {self.country_id})
        """
        return Database.connect(query, "insert")


class Address(Country):
    table_name = "address"

    def __init__(self, name, city_id):
        Country.__init__(self, name)
        self.city_id = city_id

    @staticmethod
    def select():
        query = f"SELECT * FROM {Address.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO address(name, city_id) VALUES('{self.name}', {self.city_id})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data, table) -> str:
        if column == "id":
            query = f"UPDATE {table} SET {column} = {new_data} WHERE {column} = {old_data}"
        else:
            query = f"UPDATE {table} SET {column} = '{new_data}' WHERE {column} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data, table):
        query = f"DELETE FROM {table} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class Student():
    table_name = "student"

    def __init__(self, first_name, last_name, birth_date, address_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address_id = address_id

    @staticmethod
    def select():
        query = f"SELECT * FROM {Student.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO student(first_name, last_name, birth_date, address_id) VALUES('{self.first_name}', '{self.last_name}', '{self.birth_date}', {self.address_id})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data, table) -> str:
        if column == "id":
            query = f"UPDATE {table} SET {column} = {new_data} WHERE {column} = {old_data}"
        else:
            query = f"UPDATE {table} SET {column} = '{new_data}' WHERE {column} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data, table):
        query = f"DELETE FROM {table} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class PaymentStatus:
    table_name = "Payment_Status"

    def __init__(self, payment, student_id):
        self.payment = payment
        self.student_id = student_id

    @staticmethod
    def select():
        query = f"SELECT * FROM {PaymentStatus} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO PaymentStatus(payment, student_id) VALUES('{self.payment}', {self.student_id})
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data, table) -> str:
        if column == "id":
            query = f"UPDATE {table} SET {column} = {new_data} WHERE {column} = {old_data}"
        else:
            query = f"UPDATE {table} SET {column} = '{new_data}' WHERE {column} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data, table):
        query = f"DELETE FROM {table} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class Science:
    pass



class TimeTable:
    pass
