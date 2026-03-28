import Flow
from DB_connector import SQL_connection


library=["Admin","1234@"]

connection = SQL_connection()


def show_book():
    pass

def edit_book():
    pass


def book_menu():
    print("WELCOME TO BOOK MENU BAR")
    while True:
        print("Coices:- ")
        print("1. SHOW BOOKS")
        print("2. ADD NEW BOOK")
        print("3. EDIT BOOK")
        print("4. ADD COPY OF BOOK")
        print("0. BACK TO PREVIOUS MENU")
      
        choice = input("Enter your choice: ").strip()     
        match choice:
            case '0':
                break
            case '1':
                show_book()
            case '2':
                Flow.insertions_entries(connection)
            case '3':
                edit_book()
            case '4':
                pass       
    


def main_menu():
    while True:
        print("-"*30)
        print("Main Menu")
        print("-"*30)

        print("1 : FOR BOOK")
        print("2 : FOR MEMBER")
        print("3 : FOR ISSUE")
        print("4 : FOR RETURN")
        print("5 : FOR PAYMENTS")
        print("6 : FOR REPORTS")
        print("0 : FOR EXIT FROM MENU")

        print("-"*30)
        print("Main Menu")
        print("-"*30)

        choice=input("Enter the choice : ").strip();
        if choice == '0':
            print("BYE BYE !! ENJOY YOUR DAY..")
            break
        if choice=='1':
            book_menu()
        elif choice=='2':
            print("In Member")
        elif choice=='3':
            print("In ISSUE")
        elif choice=='4':
            print("In RETURN")
        elif choice=='5':
            print("In PAYMENT")
        elif choice=='6':
            print("In Report")
        else:
            print("CHALA JA BSDK : 😂😂😂😂😂😂")
            break
        




def login():
    user=input("Enter the username :")
    password=input("Enter the password :")

    if (library[0]==user and library[1]==password):
        main_menu()
    else:
        print("User not verified")

login()

# closing the database connection 
connection.connection_close()