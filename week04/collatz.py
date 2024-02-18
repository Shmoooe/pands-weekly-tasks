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
         number = number // 2              #Now I'm not sure what to do here.

    elif (number % 2) != 0:                #Odd numbers
         number = (3 * number) + 1         #I consulted chatGPT about these specific parts of the if/else statements
    numbers.append(number)                 #as I'd only seen print statements after an if statement

for x in numbers:
     print(x, end=" ")                     #Consulted ChatGPT for this too to learn about end=" "   


        