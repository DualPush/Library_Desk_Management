import Flow
from DB_connector import SQL_connection



library=["Admin","1234@"]

connection = SQL_connection()


def book_menu():
    while True:
        print("-"*30)
        print("WELCOME TO BOOK MENU BAR Choice")
        print("-"*30)
        print("1. SHOW BOOKS")
        print("2. ADD NEW BOOK")
        print("3. EDIT BOOK")
        print("4. ADD COPY OF BOOK")
        print("0. BACK TO PREVIOUS MENU")
        print("-"*30)
        print("Member Menu Choice")
        print("-"*30)
        choice = input("Enter your choice: ").strip()     
        match choice:
            case '0':
                break
            case '1':
                Flow.show_book(connection)
            case '2':
                Flow.insertions_entries(connection)
            case '3':
                Flow.edit_book(connection)
            case '4':
                pass       
    

# --------------Member menu-----------------
def member_menu():
    while True:
        print("-"*30)
        print("Member Menu Choice")
        print("-"*30)

        print("1 :  For adding member")
        print("2 :  For Knowing member")
        print("3 :  For Editing member")
        print("0 :  For Return to Main menu")

        print("-"*30)
        print("Member Menu")
        print("-"*30)

        choice=int(input("Enter the choice : "))
        if choice==1:
            Flow.add_member(connection)
        elif choice==2:
            Flow.show_member(connection)
        elif choice==3:
            Flow.edit_member(connection)
            print("Edit Successfully that member")
        else:
            print("Chal Bye : 👋👋👋👋👋")
            break


# ------------Main Menu Entry function------------
def main_menu():
    while True:
        print("-"*30)
        print("Main Menu")
        print("-"*30)

        print("1 : 📚 FOR BOOK ")
        print("2 : 🙍 FOR MEMBER")
        print("3 : 📝 FOR ISSUE")
        print("4 : ℹ️  FOR RETURN")
        print("5 : 💵 FOR PAYMENTS")
        print("6 : 📜 FOR REPORTS")
        print("0 : 👋 FOR EXIT FROM MENU")

        print("-"*30)
        print("Main Menu")
        print("-"*30)

        choice=int(input("Enter the choice : "))

        if choice==1:
            book_menu()
        elif choice==2:
            member_menu()
        elif choice==3:
            print("In ISSUE")
        elif choice==4:
            print("In RETURN")
        elif choice==5:
            print("In PAYMENT")
        elif choice==6:
            print("In Report")
        else:
            print("CHALA JA BSDK : 😂😂😂😂😂😂")
            break
        

# ------------Enrty Login function-----------------
def login():
    # Entering Credential
    user=input("Enter the username :")
    password=input("Enter the password :")

    # Check or verify crdential
    if (library[0]==user and library[1]==password):
        main_menu()
    else:
        print("User not verified")

login()

# closing the database connection 
connection.connection_close()