from itertools import combinations

wiki = { "a":1, "b":2 }
keys = list( wiki.keys() )
print( keys )

result = [ {} ]
for i in range( 1, len( wiki ) + 1 ):
    seq = combinations( keys, i )
    print( seq )
    for element in seq:
        print( "element {}".format( element ) )
        subdict = {}
        for key in element:
            print( key )
            subdict[key] = wiki[key]
        result.append( subdict )
print( result )
