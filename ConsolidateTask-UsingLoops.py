# Python Program to Calculate the Area of a Rectangle (Using loops to ensure input is positive)
# The program also uses if and while loops to allow the user to repeat the operation

print ("Hello. This program calculates the area of a rectangle (or square)") 

def calculate_area():
    print(" ") # Prints a blank line for readability and neatness

    length = input('Please enter the length of the rectangle:')
    
    while not length.isdigit():
        print("Error: Please enter a valid number")
        length = input('Please enter the length of the rectangle:')
    
    length = int(length) # convert to integer to check it is positive

    while length <= 0 :
        print ("Length must be positive. Try again")
        length = int(input('Please enter the length of the rectangle:'))
       
        while not length.isdigit():
            print("Error: Please enter a valid number")
            length = input('Please enter the length of the rectangle:')#checks again that length is a number

    length = int(length)  #convert length to integer after validation


    if length > 0:
        #When a positive length is entered, the programme proceeds to request the width  
        width = input("Please enter the width of the rectangle: ")

        while not width.isdigit():
            print("Error: Please enter a valid number")
            width = input('Please enter the width of the rectangle:')

        width = int(width) #convert width to integer to check it is positive
    
       #Now width is an integer, Python checks if it is positive
        while width <= 0 :  
            print ("\nThe width must be positive.Try again")
            width = input('Please enter the width of the rectangle:')

            while not width.isdigit():
                print("Error: Please enter a valid number")
                width = input("Please enter the width of the rectangle:")#checks again that width is a number

                width = int(width) #convert width to integer after validation

        if width > 0:

            area = length * width #proceeds with calculation when both length and width are positive
            print("\n The Area is", area)
            print(" ") #Prints a blank line for readability and neatness
            return area
                

calculate_area() #This core line calls the calculate_area function.

ans = int(input("Would you like to do this again. \n  1. Yes \n  2. No "))
while ans == 1:
    calculate_area()
    ans = int(input("Would you like to do this again. \n  1. Yes \n  2. No ")) #This gives the user the option to repeat the calculation

else:
    closing = input("Thanks for using the program. Bye! Press Enter to exit.")
    quit()
          
 #The above ends the program when the user confirms they do not want to repeat the operation
         
           

