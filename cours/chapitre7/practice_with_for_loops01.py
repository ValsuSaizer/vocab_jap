from pcinput import getInteger

total = 0

for x in range( 5 ):
    number = getInteger( "Please enter an integer: " )
    total += number

print( "The total is:", total )
