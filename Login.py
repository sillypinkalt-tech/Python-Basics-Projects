# This is mini login system with prefilled details 
# motive was to just make a simple login interface for a pre-saved profile 

# Hint: Default username = John Doe password = Great@123
# You can change these values if you want different credentials

# Pre-saved credentials
saved_username = "John Doe"
saved_password = "Great@123"

print("Enter your details to log into your account")

#Login Inputs

username = input("Enter your username: ")
password = input("Enter your password: ")

if(username==saved_username and password==saved_password):
    print("✅ Logged in Successfully")
else:
    print("❌ invalid Credentials, try again")
