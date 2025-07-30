import csv
import diet_choose

user_profiles = {}
user = {}#Indiviaual users, add in main dict later 

def add_New_User():
    # User data
    print(len(user_profiles))
    new_user_id = len(user_profiles) + 1#Need to change this to unique ID generation
    user['id'] = new_user_id
    user['name'] = input("Enter your name: ")
    user['password'] = input("Enter password: ")
    user['age'] = int(input("Enter your age: "))
    user['weight'] = float(input("Enter your weight (kg): "))
    user['height'] = float(input("Enter your height (cm): "))
    
    user['diet'] = user_Diet_Preffrence()

    user_profiles[new_user_id] = user

    # add to database file
    with open("users.csv", mode="a+", newline="") as file:
        file.seek(0)
        is_empty = file.read(1) == ""
        writer = csv.DictWriter(file, fieldnames=user.keys())
        if is_empty:
            writer.writeheader()
        writer.writerow(user)
    print("------------------")
    print(f"User {user['name']} added with ID {new_user_id}")
    print("------------------")

def user_Diet_Preffrence():

    print(f"Choose diet: {diet_choose.diet_rules.keys()}")
    choice = int(input("Enter your choice: "))

    if choice == 1: 
        print("You chose Keto diet")
        # user['diet'] = 'keto'
        return 'keto'

    elif choice == 2:
        print("You chose low_carb diet")
        # user['diet'] = 'low_carb'
        return 'low_carb'

    elif choice == 3:
        print("You chose high_protein diet")
        # user['diet'] = 'high_protein'
        return 'high_protein'

    elif choice == 4:
        print("You chose custom diet")
        # user['diet'] = 'custom'

        return 'custom'

add_New_User()