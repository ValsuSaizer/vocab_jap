from itertools import combinations
from pcinput import getInteger

quinte = []
while True:
    x = getInteger( "Enter numbers to process, enter 0 to start processing: " )
    if x == 0:
        break
    quinte.append( x )

possibilities = []
for y in range( 1, len( quinte ) + 1 ):
    seq = set( combinations( quinte, y ) )
    for item in seq:
        if sum( item ) == 0:
            possibilities.append( item )

if len( possibilities ) >= 1:
    print( "Here's the different combinations with the entered list:" )
    for k in possibilities:
        for num in k:
            print( num, end=" " )
        print()
else:
    print( "There's no solution for this list of numbers : {}".format( quinte ) )
