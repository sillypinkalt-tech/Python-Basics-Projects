# Library Book tracker-
# Checks if the book is available or borrowed 

library = {
    "HarryPotter": [ " Author: J.K.Rowling","Available"], #<----- lists in dict 
    "PercyJackson": [" Author: RickRiordan","Available"],
    "SherlockHolmes": [" Author: ArthurConanDoyle","Available"]
}

# Loops

while True:
    books = [" HarryPotter: Author: J.K.Rowling","PercyJackson: Author: RickRiordan","SherlockHolmes: Author: ArthurConanDoyle"]
    print("Books: ",books)

    #Taking inputs
    book = input("Enter Name of the book: ")
    status = input("Enter wether if you wanna Borrow / Return: ")

    #conditionals on basis of borrow or return
    if(status == "Borrow"):
        if(library[book][1] == "Available"):
            library[book][1]= "Unavailable"
            print("Book has been borrowed")
        else:
            print("Book is not available ")
    elif(status=="Return"):
        if(library[book][1] == "Unavailable"):
            print("The Book has been returned")
            library[book][1] = "Available"
        else:
            print("The Book was not borrowed")
         # Loops Exit 
    again = input("Want to Borrow or return? (yes/no): ").lower()
    if again != "yes":
        break



