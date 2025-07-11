# main runs the app and handles CLI interactions
from tracker import add_entry, view_summary
import random

def get_random_quote(file="data/quotes.txt"):
    try:
        with open(file, "r") as f:
            quotes = [line.strip() for line in f if line.strip()]
            return random.choice(quotes)
    except FileNotFoundError:
        return "Stay strong."


def print_menu():
    print("\n==== Macro Tracker ====")
    print("1. Add a new entry")
    print("2. View today's total macros")
    print("3. Quit")

def main():
    while True:
        print_menu()

        user_selection = input("Please select an option (1-3): \n").strip()

        if user_selection == "1":
            add_entry()
        elif user_selection == "2":
            view_summary()
        elif user_selection == "3":
            quote = get_random_quote()
            print("Exiting Macro Tracker...")
            print(quote)
            return

if __name__ == "__main__":
    main()
