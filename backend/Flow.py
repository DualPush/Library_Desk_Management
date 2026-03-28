
from Book import insertions_book
from Copy import copy






# BOOK INSERTION FUNCTION 

def insertions_entries(connection):
    # Creating Object
    book_insert = insertions_book()
    
    cursor = connection.get_cursor()

    book_insert.insert_book(cursor)
    connection.do_commit()
    connection.cursor_close()


def copy_entries(connection):
    
    book_copy = copy()
    cursor = connection.get_cursor()
    book_copy.copy_book(cursor) 
    connection.do_commit()
    connection.cursor_close()
