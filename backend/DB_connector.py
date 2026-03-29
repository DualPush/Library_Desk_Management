import mysql.connector

class SQL_connection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "127.0.0.1",
            database = "hackathon_db",
            user = "root",
            password = "manager"
        )
    
    # getting cursor for passing as a parameter
    def get_cursor(self):
         cursor = self.connection.cursor()
         return cursor
     
    # connection commitment
    def do_commit(self):
        self.connection.commit()
        
    # cursor clossing
    def cursor_close(self):
        self.connection.cursor().close()
    
    # connection closing
    def connection_close(self):
        self.connection.close()
    
         