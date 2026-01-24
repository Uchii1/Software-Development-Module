# FIBONACCI SEQUENCE PROGRAMME
# Description: Recursive Python Programme to Print Sequences of Fibonacci Numbers of a Requested Length


# In the Fibonacci sequence, every subsequent term is the sum of the two prior terms. 
# The first two Fibonacci numbers are 1 and 1. The below provides for  n == 0 to return 0; and n == 1 to return 1. 
# The next term will then be 1 (1 + 0 = 1); and then 2 (1 + 1 = 2). The subsequent terms are 3, 5, 8, 13, 21 and so on.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1 
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


# The callingFibonacci() function below accepts input and calls the programme's main fibonacci() function
def callingFibonacci():
    print("How many terms in the Fibonacci sequence do you want to print? ")
    x = input(" Number of terms to print: ").strip()  #x is accepted as a string and stripped of trailing spaces
    print(" ")  # A blank line for neatness

    # The below catches an exception where input, x, is not a positive integer or where no input is entered
    if (not x) or (not x.isdigit()) or (x == "0"):
        print("Please enter a valid positive integer as input")
        print(" ")  # A blank line for neatness
        # The callingFibonacci() function (which is thus also recursive) calls itself to give the user another attempt
        callingFibonacci()  

    # This loop uses the recursive fibonacci() function to print the first x fibonacci numbers 
    else:
        x = int(x)  # This converts x to an integer
        for p in range (1, x+1):
            m = fibonacci(p)
            # Converting the variables p and m to strings 
            p = str(p)
            m = str(m)
            print("Fibonacci number " + p + " is " + m)
        print("*" * 80)  # This leaves a line for decoration after printing the Fibonacci sequence requested.
        print(" ")  # A blank line for neatness 
        
 
# This runs the main menu, from which the user can choose whether to run the function again or exit.
def menu():
    running = True
    while running:  
        print("Would you like to do this again?\n 1.Yes\n 2.No")
        repeat = input("\nEnter an option from above (1-2): ").strip()

        # The below is executed if the user opts to run the function again
        if repeat == "1":
            callingFibonacci()

        # The below is printed if the user opts to exit the programme.
        elif repeat == "2":
            print("\nYou have chosen to exit.") 
            # Input is requested to keep the programme open until the user hits ENTER
            stayopen=  input("Press ENTER to close the programme. You can reopen the programme later to do this again.")
            break  # This ends the programme when the user presses ENTER

        # The below is executed where the user does not enter either 1 or 2.
        else:
            print("\nPlease pick a valid option")
            menu()
            

# The below runs when the programme is first opened.
print("Welcome to the Fibonacci sequence programme")
callingFibonacci()  # This calls the callingFibonacci() function, which calls the fibonacci() function for the first process.
menu()  # After the first process, menu() the main menu function, so the user can either repeat the process or exit the programme.
   




