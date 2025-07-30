# check if the meal that  added is according to a particular diet 
import pandas as pd

df = pd.read_csv("food_list_ex.csv")

diet_rules = {
    "keto": {"max_carbs": 10, 
             "min_fat": 10},
    "low_carb": {"max_carbs": 20},
    "high_protein": {"min_protein": 15},
    "custom": {"max_calories": 500}  # Optional user-defined
}

def is_keto_friendly(row):
    # Check if carbs are within keto limit
    if row['carbs'] <= diet_rules['keto']['max_carbs']:
        # Check if fat is above keto minimum
        if row['fat'] >= diet_rules['keto']['min_fat']:
            return True
    return False

def is_low_carb_friendly(row):
    return row['carbs'] <= diet_rules['low_carb']['max_carbs']

def is_high_protein_friendly(row):
    return row['protein'] >= diet_rules['high_protein']['min_protein']

def is_custom_friendly(row):
    return row['calories'] <= diet_rules['custom']['max_calories']

df['is_keto_friendly'] = df.apply(is_keto_friendly, axis=1)
df['is_low_carb_friendly'] = df.apply(is_low_carb_friendly, axis=1)
df['is_high_protein_friendly'] = df.apply(is_high_protein_friendly, axis=1)
df['is_custom_friendly'] = df.apply(is_custom_friendly, axis=1)