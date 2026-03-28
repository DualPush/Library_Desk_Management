import mysql.connector
from Book import insertions_book
from Copy import copy



connection = mysql.connector.connect(
    host = "127.0.0.1",
    database = "hackathonDB",
    user = "root",
    password = "Mayank@92Dev9"
)
cursor =connection.cursor()

def insertions_entries():
    # Creating Object
    book_insert = insertions_book()

    book_insert.insert_book(cursor)
    connection.commit()


def copy_entries():
    
    book_copy = copy()
    book_copy.copy_book(cursor) 
    connection.commit()

# copy_ent = copy_entries()
#   insertions
insertions_entries()


# making copies of the books
# copy_entries()



cursor.close()





# connectio close karo

connection.close()