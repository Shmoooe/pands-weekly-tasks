# This program receives an input of a 10 digit account number and outputs it with the last 4 digits displayed and the first 6 as "x".
# Author: Joanna Kelly

# Sliced the string and used the formatting function to "replace" the first 6 digits with Xs.
# I'm certain this is not the best way to approach this and will have to return in future.
# Consulted W3Schools, tried to use the replace() function as replace([:6], XXXXXX) but that did not work.
# This program can now account for numbers longer than 10-digits, but returns the same number of Xs as a 10-digit number.


inputAccountNumber = input("Please enter a 10 digit account number: ")

lastDigits = inputAccountNumber[-4:]


print(f"XXXXXX{lastDigits}")





