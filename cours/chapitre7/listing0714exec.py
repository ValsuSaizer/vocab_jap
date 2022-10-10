from pcinput import getInteger

while True:
    x = getInteger( "Please enter a value for x: " )
    if x >= 0:
        break
    else:
        print( "The value of x must be superior or equal to 0" )
        continue

print( "The value of x is:", x )
