# TOPIC-- marks based upon result (Only for marks under 100)

#loop 

while True:
    # Taking inputs / for marks only under 100
    name = str(input("Enter your name: "))
    marks = int(input("Enter your Total Marks: "))
    print("Student's name: ", name)

    # Conditional Statements for different grades
    if(marks>100):
        print("Invalid Number, marks limit 100")
    elif(marks <0):
        print("Invalid Number")
    elif(marks >=90):
        print("You got Grade: A")
    elif(90> marks >=80):
        print("You got Grade: B")
    elif(80> marks >= 70):
        print("You got Grade: C")
    elif(70> marks):
        print("You got Grade: D")
     # Loops Exit 
    again = input("Want to check again? (yes/no): ").lower()
    if again != "yes":
        break
