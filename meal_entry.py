# add new meals to user
import diet_choose
day_meals = []  # List to store meals for the day

def add_meal():
    meal_name = input("Enter meal name:") 

    if meal_name in diet_choose.df["food"].values:
        day_meals.append(meal_name)
        print(f"Added {meal_name}")
    else:
        print("Web scrapping")
