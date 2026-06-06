#BMI calculator - Project No- 3rd ig (lemme js push this code to github) 

#1- taking inputs
Weight = int(input("Enter your weight in kg: "))
Height = int(input("Enter your height in cm: "))

#2-CM----> M
Height /= 100

#3- BMI calculation
BMI = Weight/(Height**2)

#4- output
print("Your BMI is: ",BMI)


