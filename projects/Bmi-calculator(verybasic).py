#BMI calculator - Project No- 3rd ig (lemme js push this code to github)

while True:
    #1- taking inputs
    Weight = int(input("Enter your weight in kg: "))
    Height = int(input("Enter your height in cm: "))

    #2-CM----> M
    Height /= 100

    #3- BMI calculation
    BMI = Weight/(Height**2)

    #4- Conditionals

    if BMI < 18.5:
        print("Category: Underweight")
    elif 18.5 <= BMI < 24.9:
        print("Category: Normal")
    elif 25 <= BMI < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obese")

    #5- output
    print(f"Your BMI is: {BMI:.2f}")

    #6 Loops
    again = input("Want to check your BMI again? (yes/no): ").lower()
    if again != "yes":
        break


