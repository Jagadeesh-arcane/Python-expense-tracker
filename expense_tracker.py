import csv
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave empty for today: ").strip()
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (e.g., Food, Rent, Transport): ").strip()
    amount = input("Enter amount: ").strip()

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
        print("Expense added successfully.")

def view_expenses():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            total = 0
            print("\nDate        | Category     | Amount")
            print("-" * 35)
            for row in reader:
                date, category, amount = row
                print(f"{date:12} {category:12} ${float(amount):.2f}")
                total += float(amount)
            print("-" * 35)
            print(f"Total spent: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses found.")

def main():
    print("=== Personal Expense Tracker ===")
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Select an option: ").strip()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
