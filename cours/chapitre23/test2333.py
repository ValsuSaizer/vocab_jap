from itertools import product

seq = product( [1,2,3], "ABC", ["apple","banana"] )
for item in seq:
    print( item )
