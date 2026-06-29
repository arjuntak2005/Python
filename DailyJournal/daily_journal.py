# 26-06-26 - My first python project.

# Daily Journal: version 1:-
path = "daily_journal.txt"
from datetime import date
todays_date = date.today().strftime("%d/%m/%Y")
#date = input("Enter todays date: ")
work_done = input("Enter Work Done: ")
thoughts_feelings = input("Enter Thoughts/Feelings: ")
learnings = input("Enter Learnings: ")

with open(path, 'a') as journal:
    journal.write(f"\n\n----#---- {todays_date} ----#----")
    journal.write(
        f"\nWork Done: {work_done}\nThoughts/Feelings: {thoughts_feelings}\nLearnings: {learnings}")
    journal.write("\n-- ---- ---- ---- ---- ---- --")