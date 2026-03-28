import mysql.connector

class Insert_Book:
    def __init__(self):
        self.title=input("Enter the title : ")
        self.author=input("Enter the author : ")
        self.subject=input("Enter the subject : ")
        self.isbn=input("Enter the isbn : ")
        self.price=input("Enter the price of book :")

    def insert_book(self,cursor):
        self.cursor=cursor
        
        # Query to insert book in table
        query="""
        insert into book (title,author,isbn,price)
        values(%s,%s,%s,%s,%s)
        """

        values=(self.title,self.author,self.subject,self.isbn,self.price)

        cursor.execute(query,values)
