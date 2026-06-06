# Simple Calculator

# taking inputs
num_1 = int(input("Enter your First number: "))
num_2 = int(input("Enter your Second number: "))
operation = input("Enter your operators from (/ * + - % **): ")


# Conditional Statements
if(operation == "+"):
    print("The sum of your numbers is: ",num_1+num_2)
elif(operation == "-"):
    print("The difference of your numbersis: ",num_1-num_2)
elif(operation == "/"):
    if(num_2 == 0):
        print("Error: Division by zero not allowed")    
    else:
        print("The quotient of the Numbers is: ", num_1/num_2)
elif(operation == "*"):
    print("The product of the numbers is: ",num_1*num_2)
elif(operation == "**"):
    print("The power / exponent of number is: ", num_1**num_2)
elif(operation == "%"):
    if num_2 == 0:
        print("Error: Modulus by zero not allowed")
    else:
        print("The remainder of your numbers is:", num_1 % num_2)
else:
    print("Invalid operator ")


    
