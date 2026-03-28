
class insertions_book:
    def __init__(self):
        self.title = input("Enter book title name: ")
        self.author = input("Enter book author name: ")
        self.subject = input("Enter book subject name: ")
        self.isbn = input("Enter book ISBN: ")
        self.price = input("Enter book price: ")
        
    # isertions book records 
    
    def insert_book(self,cursor):
        self.cursor = cursor
         
        query = """ 
        insert into book (title, author, subject, isbn, price) 
        values(%s,%s,%s,%s,%s)
        """
        values = (self.title,self.author,self.subject,self.isbn,self.price)
        
        cursor.execute(query,values)      
        
class copy:
    def __init__(self): 
        self.book_id = input("Enter book ID: ")
        self.rack = input("Enter Rack A-Z defalt(A): ") or 'A'
        self.status = input("Enter status: ")
        
    def copy_book(self, cursor):
        self.cursor = cursor
        
        query = """
        insert into copy(book_id,rack,status)
        values(%s,%s,%s)
        """        
        
        values = (self.book_id,self.rack,self.status)
        
        cursor.execute(query,values)