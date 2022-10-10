from itertools import permutations

seq = permutations( ["1","2","3","4","5","6","7","8"], 1 )
for item in seq:
    for value in item:
        print( value )

