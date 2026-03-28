import time
from Book import insertions_book
from Copy import copy
from Member import AddMember,EditMember
from LibraryDesk import Library
import mysql.connector





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


# -----------Members Function--------

def add_member(connection):
    add_members=AddMember()
    cursor = connection.get_cursor()
    add_members.add_member(cursor)
    connection.do_commit()
    connection.cursor_close()

def show_member(connection):
    library=Library()
    cursor=connection.get_cursor()
    library.show_member(cursor)
    connection.cursor_close()
    time.sleep(3)

def edit_member(connection):
    edit_members=EditMember()
    cursor=connection.get_cursor()
    edit_members.edit_member(cursor)
    connection.do_commit()
    connection.cursor_close()
