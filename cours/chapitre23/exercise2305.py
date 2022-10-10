from itertools import combinations
from pcinput import getInteger

quinte = []
while True:
    x = getInteger( "Enter numbers to process, enter 0 to start processing: " )
    if x == 0:
        break
    quinte.append( x )

result = 0
y = 1
while y <= len( quinte ):
    seq = set( combinations( quinte, y ) )
    for item in seq:
        for num in item:
            result += num
        if result == 0:
            print( "Subset sum = 0 with the following sequence:" )
            for k in item:
                print( k, end=" " )
            print()
        result = 0
    y += 1
