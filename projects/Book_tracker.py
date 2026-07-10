# Library Book tracker-
# Checks if the book is available or borrowed 

library = {
    "HarryPotter": [ "J.K.Rowling","Available"], #<----- lists in dict 
    "PercyJackson": ["RickRiordan","Available"],
    "SherlockHolmes": [" ArthurConanDoyle","Available"]
}
books = [" HarryPotter: J.K.Rowling","PercyJackson: RickRiordan","SherlockHolmes: ArthurConanDoyle"]
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

book = input("Enter Name of the book: ")
status = input("Enter wether if you wanna Borrow / Return: ")

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
print("Books status:",library)


