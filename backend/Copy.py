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