from itertools import zip_longest

seq = zip_longest( "apple", "coconut", "banana", fillvalue=" ")
for item in seq:
    print( item )
