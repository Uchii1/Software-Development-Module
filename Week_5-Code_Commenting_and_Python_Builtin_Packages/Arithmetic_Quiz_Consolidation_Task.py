# WEEK 5 CONSOLIDATE TASK
# Python programme applying built-in packages to create a timed quiz and including comments for readability

# Importing the built-in packages needed
import math  # The math module handles calculations within the programme
import random # The random module generates random numbers, allowing the quiz questions to change every time the programme is run
import time  # The time module helps to record the time taken by the user to complete the quiz

# Including a suitable heading
print(" *** ARITHMETIC QUIZ *** ")

#  Input is requested here so that the programme does not proceed until the user presses the ENTER key
display_instructions = input("There are 5 questions in total. You have three attempts at each. Any valid number inputted counts as an attempt.\nHit ENTER now to start the quiz")

### TIMER BEGINS ###
mark_start = time.time()  # This marks the time the user starts the first question


# Explanatory notes are provided in detail for the first question. 
# The code for remaining questions follows a similar pattern. As such, to reduce the wordiness of the script, the explanatory notes for subsequent sections are less detailed.

# A function to check that the input is a valid integer.
# Ths function will be called during each question below.
def ensure_integer(question_text):
    while True:
        try:
            return int(input(question_text))
        except ValueError:
            print("Error: Please enter a valid integer!")  # This is printed if the input is not an integer.


# Question 1 - Squares
print("\nQuestion 1")

# This generates a random number between 1 and 10 and asks the user to enter the square of the number
mark1 = 1  # The mark awarded remains 1 unless the question is answered incorrectly even once.
wrong_count1 = 0  # This counts how many times the user enters the wrong answer for each question. The question is skipped if this exceed 2.
a = random.randint(1, 10)  # A random number between 1 and 10 inclusive is generated and labelled 'a' 
b = a ** 2  # b is a squared

# The below calls the ensure_integer function defined above, to accept only integer inputs
ans1 = ensure_integer(f"Enter the square of {a}: ")  

# This compares the user's answer (converted to an integer) to the correct answer
while ans1 != b and wrong_count1 < 3:  # This compares the user's entry with the correct answer, b.
    mark1 = 0  # The mark for the question is changed to 0 if the user inputs a wrong answer once.
    wrong_count1 += 1
    print("Try again please")  # Repeats the request for input if input is invalid
    ans1 = ensure_integer(f"Enter the square of {a}: ")  
   
if wrong_count1 == 3:
    print("The correct answer is " + str(b) + " moving to the next question...")
else:
    print("Your answer is correct")


# Question2 - Division Remainders
print("\nQuestion 2")

# Finding remainder
mark2 = 1
wrong_count2 = 0
c = random.randint(10, 100)
d = random.randint(1, 10)
e = c % d

ans2 = ensure_integer(f"What is the remainder when" + " " + str(c) + " " + "is divided by" + " " + str(d) + "? " + " ")

# This compares the user's answer (converted to an integer to the correct answer)
while ans2 != e and wrong_count2 < 3:
    print("Try again please")  # Repeats the request for input if input is invalid
    ans2 = ensure_integer(f"What is the remainder when" + " " + str(c) + " " + "is divided by" + " " + str(d) + "? " + " ")
    mark2 = 0
    wrong_count2 += 1

if wrong_count2 == 3:
    print("The correct answer is " + str(e) + " moving to the next question...")
else:
    print("Your answer is correct")


# Question 3 - Factorials
print("\nQuestion 3")

# This will request the factorial of a number between 1 and 10
mark3 = 1
wrong_count3 = 0
f = random.randint(1,6)
g = math.factorial(f)

ans3 = ensure_integer("What is the factorial of " + str(f) + "?: ")

# This compares the user's answer (converted to an integer to the correct answer)
while ans3 != g and wrong_count3 < 3:
    print("Try again please")  # Repeats the request for input if input is invalid
    ans3 = ensure_integer("What is the factorial of " + str(f) + "?: ")
    mark4 = 0
    wrong_count3 += 1

if wrong_count3 == 3:
    print("The correct answer is " + str(g) + " moving to the next question...")
else:
    print("Your answer is correct")


# Question 4 - Exponents
print("\nQuestion 4")
# This will request the value of a number less than or equal to 7 raised to number less than or equal to 3
mark4 = 1
wrong_count4 = 0
h = random.randint(1,7)
j = random.randint(0,3)
k = h ** j

ans4 =  ensure_integer("What is "+ str(h) + "^" +str(j) +"?: ")

# This compares the user's answer (converted to an integer to the correct answer)
while ans4 != k and wrong_count4 < 3:
    print("Try again please")  # Repeats the request for input if input is invalid
    ans4 =  ensure_integer("What is "+ str(h) + "^" +str(j) +"?: ")
    mark4 = 0
    wrong_count4 += 1

if wrong_count4 == 3:
    print("The correct answer is " + str(k) + " moving to the next question...")
else:
    print("Your answer is correct")


# Question 5 - Arithmetic Equations
print("\nQuestion 5")
# This will request the result of a simple arithmetic expression in the format: (m x n) + p
# For simplicity, each number in the question is coded to be less that or equal to 10
mark5 = 1
wrong_count5 = 0
m = random.randint(1,10)
n = random.randint(0,10)
p = random.randint(1,10)
ans5 = ensure_integer("Calculate:("+ str(m) + "x" + str(n) + ") + " + str(p) +": ")
q = (m*n)+p

# This compares the user's answer (converted to an integer to the correct answer)
while ans5 != q and wrong_count5 < 3:
    print("Try again please")  # Repeats the request for input if input is invalid
    ans5 = ensure_integer("Calculate:("+ str(m) + "x" + str(n) + ") + " + str(p) +": ")
    mark5 = 0
    wrong_count5 += 1

if wrong_count5 == 3:
    print("The correct answer is " + str(q) + " moving to the next question...")
else:
    print("Your answer is correct")


### TIMER STOPS ###
mark_end = time.time()  # This marks the time the user completes the final question

# Calculating the time taken by the user to complete the quiz
time_taken = mark_end - mark_start

# Scoring System and Comment
# It uses a manual calculation where each mark is added individually, to simplyfy the future addition of questions.
score = mark1 + mark2 + mark3 + mark4 + mark5

# A decrative feature before printing the score
print("Quiz Completed!")
print(" ")
print("LOADING... Please wait", end=" ")
for i in range (3):
    print(".", end= " ", flush= True)  # This prints three dots.The flush parameter ensures python displays one dot after each time interval
    time.sleep(0.75)  # This applies the time package to space the appearance of the dots out by 0.75 seconds

# Printing the final score
print(f"\n\nScore: {score}/5")  # This prints the final score, marked over 5.
print(f"\nTime Taken:{time_taken:.2f} seconds") # This returns the elapsed time in seconds to 2 decimal places

# Generating a comment based on the score
if score >= 4:
    comment = "Well Done!"  # "Well Done!" is printed if the score is 4/5 or above
elif score >= 2:  
    comment = "Good Attempt!"  # "Good Attempt!" is printed if the score is 2/5 or 3/5
else:
    comment = "Practice some more" # "Practise some more" is printed if the score is 1/5

print(comment) # The final command prints the comment.
stayopen = input("Press ENTER to exit")  # This keeps the window open until the user is ready to exit


