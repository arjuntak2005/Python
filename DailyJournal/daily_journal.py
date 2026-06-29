# 27-06-26 - Daily Journal: version 2:-
path = "DailyJournal/daily_journal.txt"
from datetime import date
todays_date = date.today().strftime("%d/%m/%Y")


def Mode_Input():
    try:
        return int(input("\nEnter: '1'-Write Mode | '2' -Read Mode | '3' -Close   -> "))
    except ValueError:
        print("\nYou are supposed to enter one of the number mentioned above!")
        return None


def Mode_Selection():
    while True:
        mode_input = Mode_Input()
        if mode_input == 1:
            print("You are in Write Mode")
            Write_Mode()
        elif mode_input == 2:
            print("You are in Read Mode")
            Read_Mode()
        elif mode_input == 3:
            print("Closed..")
            break
        else:
            print("Invalid input Try Again.")


def Write_Mode():
    # Taking Inputs
    print("Please enter following details: ")
    work_done = input("Work Done: ")
    thoughts_feelings = input("Thoughts/Feelings: ")
    learning = input("Learning: ")
    # Appending data to file
    with open(path, 'a') as journal:
        journal.write(f"\n\n----#---- {todays_date} ----#----")
        journal.write(
            f"\nWork Done: {work_done}\nThoughts/Feelings: {thoughts_feelings}\nLearning: {learning}")
        journal.write("\n-- ---- ---- ---- ---- ---- --")
    print("Data added Successfully")


def Read_Mode():
    # Opening file in read mode
    print("Here is your file Content:\n")
    try:
        with open(path) as journal:
            content = journal.read()
            print(content)
    except FileNotFoundError:
        print("No journal file found yet. Write something first!")


def Footer():
    print("\n               Stay consistent!")
    print("                    -ART\n")


# User Template:
print("\n~~~ Welcome to Daily Journal ~~~")
Mode_Selection()
Footer()