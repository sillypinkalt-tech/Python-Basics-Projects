# Grade analyzer - sorts out no. of students on basis of grades
# loops

while True: 
    Grades = input("Enter each grades separated by spaces (E.g.- A B C D)(Only-A B C D F): ")
    Grade = Grades.split()   # turns input string into list

    print("Total Number of Students: ",len(Grade))

    # Printing Numbers of Students acc to grades
    print("A:",Grade.count("A"),"Students")
    print("B:",Grade.count("B"),"Students")
    print("C:",Grade.count("C"),"Students")
    print("D:",Grade.count("D"),"Students")
    print("F:",Grade.count("F"),"Students")

    # Percentage of grades acc to students
    print(f"Percentage of A graders:{((Grade.count("A")/len(Grade))*100):.2f}%")
    print(f"Percentage of B graders:{((Grade.count("B")/len(Grade))*100):.2f}%")
    print(f"Percentage of C graders:{((Grade.count("C")/len(Grade))*100):.2f}%")
    print(f"Percentage of D graders:{((Grade.count("D")/len(Grade))*100):.2f}%")
    print(f"Percentage of E graders:{((Grade.count("E")/len(Grade))*100):.2f}%")
    
     # Loops Exit 
    again = input("Want to check again? (yes/no): ").lower()
    if again != "yes":
        break
