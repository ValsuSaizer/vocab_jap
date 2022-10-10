from itertools import permutations

seq = permutations( [1,2,3], 3 )
for item in seq:
    print( item )
