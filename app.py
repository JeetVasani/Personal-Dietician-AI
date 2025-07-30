# # # main file to run
import diet_choose
import user_add
import meal_entry

day_meals = []

def options_for_user():#Main loop
    while True:
        print("Welcome User!")
        print("------------------")
        print("1.Enter new meal")
        print("2.Change User Data")
        print("3.Exit to main menu")
        print("-1.Quit")
        print("------------------")
        choise = int(input("Enter choice:"))
        print("------------------")

        if choise == 1:
            meal_entry.add_meal()
        
        elif choise == 2:
            pass
        
        elif choise == -1:
            print("Exiting to main menu...")
            break
        
def main_Menu():
    print("1. Login")
    print("2. Register")
    choice = int(input("Enter your choice: "))
    print("------------------")

    if choice == 1:
        login_user()
    elif choice == 2:
        user_add.add_New_User()#Change user id 
        options_for_user()
    else:
        print("Invalid choice, please try again.")

    options_for_user()

def login_user():
    user_Id = input("Enter user id: ")
    password = input(f"Enter user password for {user_Id}: ")     
    # Check the user ID and password against user database

    if user_Id in user_add.user_profiles and user_add.user_profiles[user_Id]['password'] == password:
        options_for_user()
    else:
        print("Invalid user ID or password. Please try again.")
        password = input(f"Enter user password for {user_Id}: ")     


main_Menu()