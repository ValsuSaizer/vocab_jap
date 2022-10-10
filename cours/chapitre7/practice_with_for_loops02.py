from pcinput import getInteger

count = getInteger( "Please enter an integer for count: " )

for x in range( count, 0, -1 ):
    print( x )

print( "Blast off!" )
