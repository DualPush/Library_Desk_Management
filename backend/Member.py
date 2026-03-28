class Member:
    def __init__(self):
        self.name=input("Enter the name of member : ")
        self.email=input("Enter the name of email : ")
        self.phone=input("Enter the name of phone : ")

    def add_member(self,cursor):
        self.cursor=cursor

        query="""
        insert into member(name,email,phone)
        values (%s,%s,%s)
        """

        values=(self.name,self.email,self.phone)

        cursor.execute(query,values)  

