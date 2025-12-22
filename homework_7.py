import sqlite3


def create_table():

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()


    cursor.executemany("""
    INSERT INTO books (
        name, author, publication_year, genre, number_of_pages, number_of_copies
    ) VALUES (?, ?, ?, ?, ?, ?)
    """, [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("Animal Farm", "George Orwell", 1945, "Political satire", 112, 7),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 4),
        ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, "Fantasy", 223, 10),
        ("The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fairy tale", 96, 6),
        ("Fahrenheit 451", "Ray Bradbury", 1953, "Science fiction", 249, 3),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Classic", 281, 5),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Classic", 277, 4),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Classic", 671, 2),
        ("Pride and Prejudice", "Jane Austen", 1813, "Romance", 432, 3)
    ])

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    insert_books()
    print("Таблица создана, данные успешно добавлены.")
