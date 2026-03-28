class Library:
    def __init__(self):
        pass
    
    # for printing book table
    def book_data(self,cursor):
        self.cursor = cursor
        print('-'*10)
        print("BOOK DATA")
        query = """
        select * from book
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        print('-'*90)
        print(f"{'BOOK_ID'}| {'TITLE':<15}| {'AUTHOR':<15}| {'SUBJECT':<15}| {'ISBN':<15}| {'PRICE':<15}")
        print('-'*90)
        for row in rows:
            book_id, title, author, subject, isbn, price = row
            print(f"{book_id:<7}| {title:<15}| {author:<15}| {subject:<15}| {isbn:<15}| {price:<15}")         
        print('-'*90)
        
    def edit_book(self,cursor):
        self.cursor = cursor
        self.book_data(cursor)
        b_id = int(input("Select book id: ").strip())
        column = input("Select column name: ").strip().lower()
        val = input("Enter correct value: ")
        #  Allow only valid columns
        allowed_columns = ['title', 'author','subject', 'isbn', 'price']
    
        if column not in allowed_columns:
            print("Invalid column!")
            return

        #Convert type if needed
        if column == 'price':
            val = float(val)

        try:
            query = f"UPDATE book SET {column} = %s WHERE id = %s"
            cursor.execute(query, (val, b_id))
            print("Book updated successfully")

        except Exception as e:
            print(" Error:", e)
        
        
        