from itertools import permutations

word = input( "Enter a word: " )
seq = permutations( word )
verif = []
for item in seq:
    if item not in verif:
        verif.append( item )
        print( item )
    continue
