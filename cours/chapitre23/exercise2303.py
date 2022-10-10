from itertools import permutations

word = input( "Enter a word: " )
seq = permutations( word )
for item in seq:
    print( item )
