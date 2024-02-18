# D I S A S T E R


# A program that asks the user to input any positive integer
# and ouputs the successive values of the following calculation.
# At each step it will calculate the next value by taking the current value and
# if it is even, divide it by two
# but if it's odd, multiply it by three and one.
# The program will end if the current value is one.

# Author: Joanna Kelly

# list_of_numbers = []

# number = int(input("Please enter a positive integer: "))

def collatz(number):
        if (number % 2) == 0:
            result = number // 2
        elif (number % 2) != 0:
            result = 3 * number + 1

        while result == 1:
             print(result)
             sys.exit()

        while result != 1:
             print(result)
             number = result
             return collatz(number)
        
print("Enter a positive integer: ")


# list_of_numbers.append(number)

#print([list_of_numbers])
