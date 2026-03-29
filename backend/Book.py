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
        print("Added Book successfully")      
