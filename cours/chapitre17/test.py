from pcinput import getInteger

num = getInteger( "Please enter a number: " )
if num == 0:
    print( "Dividing by zero is not allowed" )
else:
    print( "3 divided by {} is {}".format( num, 3/num ) )
print( "Goodbye!" )
