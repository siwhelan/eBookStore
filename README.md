# eBookStore 📚📖🧑‍🏫

Welcome to the Ebookstore management system! With this program, you can easily enter new books, view the books in your store, update book quantities, and delete books.


## Features

    -> Add new books to your store by entering the book ID, title, author, and quantity
    -> View a list of all the books in your store, along with their ID, title, author, and quantity
    -> Update the quantity of a particular book in your store
    -> Delete a book from your store
    

## Requirements

    Python 3
    SQLite
    

## Installation

To install the Ebookstore program, follow these steps:

  Clone the repository to your local machine:
    
    git clone https://github.com/siwhelan/eBookStore
    
  Navigate to the repository directory:
  
    cd ebookstore

  Run the program:
  
    python ebookstore.py
    
    
## Proactive Defensive Programming and Error Handling

Robustness and user-friendliness is paramount. To achieve this, proactive defensive programming and error handling techniques have been implemented to ensure that the program can gracefully handle invalid or unexpected input.

For example, in the enter_book() function, there is a check to ensure the book ID is a positive integer and that the title and author are non-empty strings. If the user enters invalid input, an exception is raised and the user is prompted to try again. This helps to prevent the program from crashing and ensures that the user knows what went wrong.

Similarly, in the view_books(), update_book(), and delete_book() functions, we check that the user has entered a valid book ID before performing any actions on the database. This ensures that the program does not crash if the user enters an ID that does not exist in the database.

Overall, these error handling techniques help to make the program more reliable and user-friendly.


## Feedback

If you have any feedback, please reach out to me at simon@swhelan.dev
