from classes import Country, City, Address, Student, Science, TimeTable


def country_tables():
    services = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
            >>>""")
    if services == '1':
        Country.select()
        back = input("""
            0.Back
                >>>""")
        if back == "0":
            return country_tables()
    elif services == '2':
        name = input("Enter your country's name: ")
        country = Country(name)
        print(country.insert())
        return country_tables()

    elif services == '3':
        column = input("Enter column name, please: ")
        old_data = input("Enter old_data: ")
        new_data = input("Enter new_data: ")
        print(Country.update(column, new_data, old_data, "country"))
        return country_tables()

    elif services == '4':
        column = input("Enter column name, please: ")
        data = input("Enter data: ")
        print(Country.delete(column, data, "country"))
        return country_tables()


def city_tables():
    services = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
            >>>""")
    if services == '1':
        City.select()
        back = input("""
            0.Back
                >>>""")
        if back == "0":
            return city_tables()
    elif services == '2':
        name = input("Enter your city's name: ")
        country_id = int(input("Enter your country's id: "))
        city = City(name, country_id)
        print(city.insert())
        return city_tables()

    elif services == '3':
        column = input("Enter column name, please: ")
        old_data = input("Enter old_data: ")
        new_data = input("Enter new_data: ")
        print(City.update(column, new_data, old_data, "city"))
        return city_tables()

    elif services == '4':
        column = input("Enter column name, please: ")
        data = input("Enter data: ")
        print(City.delete(column, data, "city"))
        return city_tables()


def address_tables():
    services = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
            >>>""")
    if services == '1':
        Address.select()
        back = input("""
            0.Back
                >>>""")
        if back == "0":
            return address_tables()
    elif services == '2':
        name = input("Enter your address name: ")
        city_id = int(input("Enter your city's id: "))
        address = Address(name, city_id)
        print(address.insert())
        return address_tables()

    elif services == '3':
        column = input("Enter column name, please: ")
        old_data = input("Enter old_data: ")
        new_data = input("Enter new_data: ")
        print(Address.update(column, new_data, old_data, "address"))
        return address_tables()

    elif services == '4':
        column = input("Enter column name, please: ")
        data = input("Enter data: ")
        print(Address.delete(column, data, "address"))
        return address_tables()


def student_tables():
    services = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
            >>>""")
    if services == '1':
        Student.select()
        back = input("""
            0.Back
                >>>""")
        if back == "0":
            return student_tables()

    elif services == '2':
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        birth_date = input("Enter your birth date: ")
        address_id = input("Enter your address id: ")
        student = Student(first_name, last_name, birth_date, address_id)
        print(student.insert())
        return student_tables()

    elif services == '3':
        column = input("Enter column name, please: ")
        old_data = input("Enter old_data: ")
        new_data = input("Enter new_data: ")
        print(Student.update(column, new_data, old_data, "student"))
        return student_tables()

    elif services == '4':
        column = input("Enter column name, please: ")
        data = input("Enter data: ")
        print(Student.delete(column, data, "student"))
        return student_tables()


def payment_status_tables():
    services = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
            >>>""")
    if services == '1':
        Payment_Status.select()
        back = input("""
            0.Back
                >>>""")
        if back == "0":
            return payment_status_tables()

    elif services == '2':
        payment = input("Enter payment status: ")
        student_id = int(input("Enter student id: "))
        student = Student(payment, student_id)
        print(student.insert())
        return student_tables()

    elif services == '3':
        column = input("Enter column name, please: ")
        old_data = input("Enter old_data: ")
        new_data = input("Enter new_data: ")
        print(Student.update(column, new_data, old_data, "student"))
        return student_tables()

    elif services == '4':
        column = input("Enter column name, please: ")
        data = input("Enter data: ")
        print(Student.delete(column, data, "student"))
        return student_tables()


def science_tables():
    pass


def time_table_tables():
    pass


def main():
    tables = input("""
        1.Country
        2.City
        3.Address
        4.Student
        5.Payment Status
        6.Science
        7.Time_table
                >>>""")

    if tables == '1':
        return country_tables()

    elif tables == '2':
        return city_tables()

    elif tables == '3':
        return address_tables()

    elif tables == '4':
        return student_tables()

    elif tables == '5':
        return payment_status_tables()

    elif tables == '6':
        return science_tables()

    elif tables == '7':
        return time_table_tables()

    else:
        print("You entered incorrect number, please try again")
        return main()


if __name__ == "__main__":
    main()
