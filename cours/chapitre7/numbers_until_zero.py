from pcinput import getInteger

num = getInteger( "Please enter a number (0 to end it): " )
count = 0
total = 0

while num != 0:
    total += num
    count += 1
    num = getInteger( "Please enter a number (0 to end it): " )

print( "The total is: ", total )
print( "The average is: ", total / count )
