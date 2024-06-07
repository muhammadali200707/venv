from manage import Database


def create_table():
    country = f"""
        CREATE TABLE country(
            id SERIAL PRIMARY KEY,
            name VARCHAR(400),
            create_date TIMESTAMP DEFAULT now());"""

    city = f"""
        CREATE TABLE city(
            id SERIAL PRIMARY KEY,
            name VARCHAR(400),
            country_id INT REFERENCES country(id),
            create_date TIMESTAMP DEFAULT now());"""

    address = f"""
        CREATE TABLE address(
            id SERIAL PRIMARY KEY,
            name VARCHAR(400),
            city_id INT REFERENCES city(id),
            create_date TIMESTAMP DEFAULT now());"""

    student = f"""
        CREATE TABLE student(
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            birth_date DATE, 
            address_id INT REFERENCES address(id),
            create_date TIMESTAMP DEFAULT now());"""

    payment_status = f"""
        CREATE TABLE payment_status(
            id SERIAL PRIMARY KEY,
            payment VARCHAR(255),
            student_id INT REFERENCES student(id),
            create_date TIMESTAMP DEFAULT now());"""

    science = f"""
        CREATE TABLE science(
            id SERIAL PRIMARY KEY,
            name VARCHAR(400),
            description VARCHAR(1000),
            price NUMERIC,
            student_id INT REFERENCES student(id),
            create_date TIMESTAMP DEFAULT now());"""

    time_table = f"""
        CREATE TABLE time_table(
            id SERIAL PRIMARY KEY,
            time VARCHAR(150),
            student_id INT REFERENCES student(id),
            create_date TIMESTAMP DEFAULT now());"""

    data = {
        "country": country,
        "city": city,
        "address": address,
        "student": student,
        "payment_status": payment_status,
        "science": science,
        "time": time_table}
    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()
