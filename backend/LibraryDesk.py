from tabulate import tabulate

class Library:
    def __init__(self):
        pass

    def show_member(self,cursor):

        query="""
        select id,name from member
        """
        cursor.execute(query)
        rows=cursor.fetchall()
        # Print table header
        print(tabulate(rows, headers=["ID", "Name"], tablefmt="grid"))

    