# tracker handles logic for adding and viewing macros
import json
from datetime import date
from pathlib import Path

#this is where the macros are stored
DATA_FILE = Path("data/entries.json")

#prep the data to be read
def load_data():
    if DATA_FILE.exists():
        with open("data/entries.json", "r") as f:
            return json.load(f)
    else:
        return {}

#add the new macro data
def save_data(data):
    with open("data/entries.json", "w") as f:
        json.dump(data, f, indent=2)

#obtain cals, protein, carbs, fats, and sodium from command-line
def add_entry():
    food = input("Food name: ").strip()
    try:
        calories = float(input("Calories: "))
        protein = float(input("Protein (g): "))
        carbs = float(input("Carbs (g): "))
        fats = float(input("Fats (g): "))
        sodium = float(input("Sodium (mg): "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    #load the previous entries for the day if needed
    today = str(date.today())
    data = load_data()
    if today not in data:
        data[today] = []

    #add the new macro data to today's entry
    data[today].append({
        "food": food,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fats": fats,
        "sodium": sodium
    })

    #save the new macros to file
    save_data(data)
    print(f"{food} added successfully!")

#output the total macros for the day
def view_summary():
    today = str(date.today())
    data = load_data()

    if today not in data or not data[today]:
        print("No entries added.")
        return

    total_calories = total_protein = total_carbs = total_fats = total_sodium = 0

    for entry in data[today]:
        total_calories += entry["calories"]
        total_protein += entry["protein"]
        total_carbs += entry["carbs"]
        total_fats += entry["fats"]
        total_sodium += entry["sodium"]

    print(f"\n---Today's Macros ({today})---")
    print(f"Calories: {total_calories}")
    print(f"Protein: {total_protein}")
    print(f"Carbs: {total_carbs}")
    print(f"Fats: {total_fats}")
    print(f"Sodium: {total_sodium}")


