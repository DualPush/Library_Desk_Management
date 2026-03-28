import mysql.connector
from Book import insertions_book
from Book import copy



connection = mysql.connector.connect(
    host = "127.0.0.1",
    database = "hackathon_db",
    user = "root",
    password = "manager"
)
cursor =connection.cursor()

def insertions_entries():
    title = input("Enter book title name: ")
    author = input("Enter book author name: ")
    subject = input("Enter book subject name: ")
    isbn = input("Enter book ISBN: ")
    price = input("Enter book price: ")
        
    book_insert = insertions_book(title,author,subject,isbn,price)
    book_insert.insert_book(cursor)


def copy_entries():
    book_id = input("Enter book ID: ")
    rack = input("Enter Rack A-Z defalt(A): ") or 'A'
    status = input("Enter status: ")
    
    book_copy = copy(book_id,rack,status)
    book_copy.copy_book(cursor) 


#   insertions
#   insertions_entries()


# making copies of the books
copy_entries()


connection.commit()
cursor.close()





# connectio close karo

connection.close()