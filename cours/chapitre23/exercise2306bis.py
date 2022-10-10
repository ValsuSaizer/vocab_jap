from itertools import combinations

wiki = { "a":1, "b":2 }
keys = list( wiki.keys() )
entries = list( wiki.values() )
#print( entries )

result = []
for i in range( 0, len( wiki ) + 1 ):
    seq = list( combinations( wiki, i ) )
    for element in seq:
        print( element )
        print( type( element ) )
        if len( element ) == 0:
            result.append( {} )
#        else:
#print( result )
