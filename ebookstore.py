import sqlite3

# create a connection to the database
db = sqlite3.connect("ebookstore.db")

# create a cursor
cursor = db.cursor()

# ===== Functions to perform user inputted requests ===== #


# Function to allow user top enter a new book


def enter_book():
    id = input("Enter the book ID: ")
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    qty = input("Enter the quantity: ")

    # Check that the book ID is a number
    try:
        id = int(id)
        if id <= 0:
            raise ValueError
    except ValueError:
        print("Invalid book ID - please enter the correct number.")
        return

    # Check that the title is a non-empty string
    if not title:
        print("Invalid title, please try again.")
        return

    # Check that the author is a non-empty string
    if not author:
        print("Invalid author, please try again.")
        return

    # Check that the quantity is a number
    try:
        qty = int(qty)
        if qty <= 0:
            raise ValueError
    except ValueError:
        print("Invalid quantity, please try again.")
        return

    # Check if book with same ID already exists
    cursor.execute(
        """
        SELECT * FROM books
        WHERE id = ?
    """,
        (id,),
    )
    result = cursor.fetchone()

    # If the book ID already exists, 'result' will be truthy - meaning the entered ID is already in the database
    # An error message is printed and the user is returned to the main menu to try again
    if result:
        print("Book with same ID already exists, please try again")
        return

    # Insert new book
    cursor.execute(
        """
        INSERT INTO books (id, title, author, qty)
        VALUES (?, ?, ?, ?)
    """,
        (id, title, author, qty),
    )
    db.commit()
    print("Book added successfully!")


# Function to allow user to update an entry, asking which detail they'd like to edit


def update_book():

    id = input("Enter the book ID: ")
    print("What do you want to update?")
    print("1. Title")
    print("2. Author")
    print("3. Quantity")
    data = input("Enter your choice: ")

    # Check that the book ID is a number
    try:
        id = int(id)
        if id <= 0:
            raise ValueError
    except ValueError:
        print("Invalid book ID - please enter the correct number.")
        return

    # Check that the data is a valid choice (either 1, 2, or 3)
    if data not in ["1", "2", "3"]:
        print("Invalid choice")
        return

    # Check that the updated title (if applicable) is a non-empty string
    if data == "1":
        title = input("Enter the new book title: ")
        if not title:
            print("Invalid title, please try again.")
            return

    # Check that the updated author (if applicable) is a non-empty string
    if data == "2":
        author = input("Enter the new book author: ")
        if not author:
            print("Invalid author, please try again.")
            return

    # Check that the updated quantity (if applicable) is a number
    if data == "3":
        qty = input("Enter the new quantity: ")
        try:
            qty = int(qty)
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Quantity must be a number.")
            return

    if data == "1":
        cursor.execute(
            """
            UPDATE books
            SET title = ?
            WHERE id = ?
        """,
            (title, id),
        )
    elif data == "2":
        cursor.execute(
            """
            UPDATE books
            SET author = ?
            WHERE id = ?
        """,
            (author, id),
        )
    elif data == "3":
        cursor.execute(
            """
            UPDATE books
            SET qty = ?
            WHERE id = ?
        """,
            (qty, id),
        )

    db.commit()
    print("Book updated successfully!")


# Function to delete a book from the database based on user inputted book ID


def delete_book():
    book_id = input("Enter the book ID: ")

    # Check that the book ID is a number
    try:
        book_id = int(book_id)
        if book_id <= 0:
            raise ValueError
    except ValueError:
        print("Invalid book ID. ID must be a number.")
        return

    # Check if book with given ID exists in the database
    cursor.execute(
        """
        SELECT * FROM books
        WHERE id = ?
    """,
        (book_id,),
    )
    result = cursor.fetchone()

    # If the book was not found in the database, print an error message and return the user to the main menu

    if not result:
        print("That book ID does not exist. Please try again.")
        return
    # Delete the book from the database
    cursor.execute(
        """
        DELETE FROM books
        WHERE id = ?
    """,
        (book_id,),
    )
    db.commit()
    print("Book deleted successfully!")


# Function to search the database for a specific book and print it's details


def search_book():

    book_id = input("Enter the book ID: ")
    cursor.execute(
        """
        SELECT * FROM books
        WHERE id = ?
    """,
        (book_id,),
    )
    result = cursor.fetchone()

    if result:
        print(
            f"\nID: {result[0]}, Title: {result[1]}, Author: {result[2]}, Quantity: {result[3]}"
        )
    else:
        print("Book not found.")


# Function to display all the books in the database


def display_books():

    cursor.execute(
        """
        SELECT * FROM books
    """
    )
    results = cursor.fetchall()

    if results:
        for result in results:
            print(
                f"ID: {result[0]}, Title: {result[1]}, Author: {result[2]}, Quantity: {result[3]}"
            )
    else:
        print("No books found.")


# Try to create the table - if doesn't already exist, the db is created

try:
    cursor.execute(
        """
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            qty INTEGER,
            UNIQUE(id)
        )
    """
    )
    db.commit()
    print("Database created successfully!")
except sqlite3.OperationalError:
    pass


# insert sample data into the table or ignore if it already exists
cursor.execute(
    """
    INSERT OR IGNORE INTO books (id, title, author, qty)
    VALUES (3001, 'A Tale of Two Cities', 'Charles Dickens', 30)
"""
)
cursor.execute(
    """
    INSERT OR IGNORE INTO books (id, title, author, qty)
    VALUES (3002, 'Harry Potter and the Philosophers Stone', 'J.K. Rowling', 40)
"""
)
cursor.execute(
    """
    INSERT OR IGNORE INTO books (id, title, author, qty)
    VALUES (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25)
"""
)
cursor.execute(
    """
    INSERT OR IGNORE INTO books (id, title, author, qty)
    VALUES (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37)
"""
)
cursor.execute(
    """
    INSERT OR IGNORE INTO books (id, title, author, qty)
    VALUES (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
"""
)
db.commit()

# ===== Main Menu ===== #

# Main menu for user to select an option #

while True:

    print("\nWelcome to the ebookstore database! What would you like to do?")
    print("1. Enter a new book")
    print("2. Update an existing book")
    print("3. Delete a book")
    print("4. Search for a book")
    print("5. Display all books")
    print("6. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        enter_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        display_books()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")


# Close the connection to the database
db.close()
