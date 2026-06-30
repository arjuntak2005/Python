#Expense Tracker v1
from datetime import date
import json

path = "ExpenseTracker/expense_tracker.json"


def get_data():
    with open(path) as file:
        return json.load(file)


def set_data(data):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


def reset_data():
    reset = {"currency": "INR", "categories": [
        "Personal", "Dining out", "Educational", "Fees", "Home", "Medication"], "expenses": []}
    set_data(reset)


def set_expense(amount: int, category, notes: str = ""):
    temp_data = get_data()
    expense = {
        "id": (len(temp_data["expenses"])) + 1,
        "date": date.today().strftime("%d-%m-%Y"),
        "amount": amount,
        "category": category,
        "notes": notes
    }
    temp_data["expenses"].append(expense)
    set_data(temp_data)

    print("\nExpense added: ", json.dumps(expense, indent=4))


def add_expense():
    # selecting category
    data = get_data()
    print("\nEnter number to select category- ")
    for i, c in enumerate(data["categories"]):
        print(f"{i+1}. {c}")
    category = data["categories"][int(input("> ")) - 1]
    print(f"{category} selected")
    # input amount and notes
    amount = int(input("\nEnter amount: "))
    notes = input("\n(Optional) Note: ")

    set_expense(amount, category, notes)


def del_expense(id):
    id -= 1
    temp_data = get_data()
    new_data = []
    deleted = []
    for i, e in enumerate(temp_data["expenses"]):
        if i == id:
            deleted.append(e)
            continue
        if i > id:
            e = dict(e)
            e["id"] -= 1
        new_data.append(e)

    print("Are you sure you want to delete: ", json.dumps(deleted, indent=4))
    print("Note : Deletion is permanent.")
    attempts = 2
    for i in range(attempts):
        user_input = input("Continue to delete, Enter (Y/N): ").strip().upper()
        match user_input:
            case "Y":
                temp_data["expenses"] = new_data
                set_data(temp_data)
                print("Expense Deleted!")
                break
            case "N":
                print("Deletion is Canceled!")
                break
            case _:
                print("Invalid Input ❌")
                if i == attempts - 1:
                    print("Limit Exceded; Deletion is Canceled!")


def get_stats():
    data = get_data()
    print("\n - - - - - - - - - -")
    print("Stats: ")
    totals = {}
    total = sum(i["amount"] for i in data["expenses"])
    totals["Total"] = total
    for i in data["expenses"]:
        a = i["amount"]
        c = i["category"]
        if c not in totals:
            totals[c] = 0
        totals[c] += a
    # Print data
    for c, a in totals.items():
        print(f"  {c}: {a}")
    print(" - - - - - - - - - -")


# Start-------
print("\n~~~ Welcome to Expense Tracker ~~~")
while True:
    get_stats()
    print("\nNavigation:")
    match input("A - Add Expense, B - Delete Expense\n> ").strip().upper():
        case "A":
            print("\nAdding new expense..")
            add_expense()
        case "B":
            id = int(input("\nEnter ID to delete: "))
            del_expense(id)
        case _:
            print("Invalid Input ❌")
