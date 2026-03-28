class AddMember:
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


class EditMember:
    def __init__(self):
        self.id=int(input("Enter the id of member : "))
        self.name=input("Enter the updated name : ")
        self.email=input("Enter the updated email : ")

    def edit_member(self,cursor):
        self.cursor=cursor

        query="""
        update member
        set name=%s,email=%s
        where id=%s
        """
        values=(self.name,self.email,self.id)
        cursor.execute(query,values)

