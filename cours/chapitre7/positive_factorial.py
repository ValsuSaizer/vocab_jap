from pcinput import getInteger

number = getInteger( "Please enter an integer: " )
total = 1

while number > 0:
    total *= number
    number -= 1

print( "The factorial of the entered number is:", total )
