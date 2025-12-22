import sqlite3

def create_tables(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)

def add_student(connection, name, age, city):
    connection.execute("""
    INSERT INTO students VALUES ('Anvar', 17, 'Bishkek')
    """)
    connection.commit()

if __name__ == "__main__":
    conn = sqlite3.connect('database.db')

    create_tables(conn)
    