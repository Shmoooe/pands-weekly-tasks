# A program that reads in a positive integer and perfroms the collatz conjecture.
# The program ends when it reaches one.

# Author: Joanna Kelly

# My idea is to create a while loop with if statements to preform the dividing, multiplying and addition.
# I will need to append the calculated results to a list, to be displayed at the end of the program.
# I will need to figure out how to format the list to print it in the specified way.

number = int(input("Please enter a positive integer: "))

numbers = []

while number != 1:
    if (number % 2) == 0:                  #Even numbers
         number = number // 2              

    elif (number % 2) != 0:                #Odd numbers
         number = (3 * number) + 1         
    numbers.append(number)                #.append will add to our list

for x in numbers:
     print(x, end=" ")                    # prints a space between the integers in the list   


        