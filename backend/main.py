library=["Admin","1234@"]


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
        if choice==1:
            print("IN BOOK")
        elif choice==1:
            print("In Member")
        elif choice==2:
            print("In ISSUE")
        elif choice==3:
            print("In RETURN")
        elif choice==4:
            print("In PAYMENT")
        elif choice==5:
            print("In Report")
        else:
            print("BYE BSDK : 😂😂😂😂😂😂")
            break
        




def login():
    user=input("Enter the username :")
    password=input("Enter the password :")

    if (library[0]==user and library[1]==password):
        main_menu()
    else:
        print("User not verified")

login()