# A Dice-Stimulator for use in Board Games
# The program rolls a six-figure dice for a specified number of interations.

# This collects the required number of die rolls and creates a variable, counting, which helps the program track the die rolls
print("Welcome to the die stimulator.")
diceNum = int(input("How many die are you rolling. For simplicity, We suggest rolling up to five die  " ))
counting = diceNum + 1

# The random() module is called so it can be used to produce random integers in the range of 1 to 6
import random
x = 1

# Creating a list to store the value of die rolls, so these can be added later
rollResults= []

#The rolling of the dice takes place in this while loop
while x <= (diceNum):
   
    x = str(x)
    diceName = ("Roll " + x + " is ")
    diceValue = random.randint(1,6)

    print(diceName + str(diceValue))
    x = int(x)
    x += 1
    rollResults.append(diceValue)
    if x > counting:
        break

# The program adds the die roll values, convert the sum to a string, and prints it
addition = sum(rollResults)
print("The sum of the rolls is " + str(addition))
x= input("Have a Great Day!")



