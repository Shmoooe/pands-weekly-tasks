# Hopefully this program will read in a positive float and ouput its approximate square root.
# Author: Joanna Kelly

#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo

# number = original number
# guess = approx square root (number/2)
# the difference in the approx root value needs to be less than the precision value
# so we need to set a precision value


def sqrt(number, precision = 10 **(-10)):
    guess = (number) / 2   # Common way to "guess" is to divide the original number by 2
    while True: # Creates a loop until the condition is met
        new_guess = (guess + number / guess) / 2  # Newton's method requires us to keep reiterating this formula until we arrive at the closest value to the actual square root.
        if abs(new_guess - guess) < precision:  # abs() returns the absolute value or positive value
            return new_guess
        guess = new_guess       # the original guess becomes the "new_guess" until the difference between the guess and the new guess is less than the precision value



number = float(input("Please enter a positive number: "))
if number <= 0:
    float(input("Please enter a positive float number: "))
    
result = sqrt(number) # Using the function created above to find the square root of the input float
clean_result = round(result, 1) # rounds a number to 1 decimal place
print(f"The square root of {number} is approx {clean_result}")


    