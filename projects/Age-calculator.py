#tryna do some project for my guthub let's see
from datetime import datetime

# Loops starts

while True:
    print("Find 🙌 your age precisely by your birth date: ")
    print("===============================================")
    birth_year = int(input("Enter your birth year (e.g., 1990): "))
    birth_month = int(input("Enter your birth month (1-12): "))
    birth_day = int(input("Enter your birth day (1-31): "))

    current_date = datetime.now()
    birth_date = datetime(birth_year, birth_month, birth_day)

    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_month, birth_day))
    print("Your age is: ", age)
    
    #Exit statement
    again = input("Do you want to calculate age again? (yes/no): ").lower()

    if again != "yes":
        break
