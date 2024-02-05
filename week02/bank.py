#bank.py
#to add the sum of two ammounts added by the user
#author: Joanna Kelly


number = int(input('Please enter an amount in cent: '))
number2 = int(input('How much would you like to add? '))
newNumber = number + number2
print(f"The sum of these is €{newNumber/100}")


