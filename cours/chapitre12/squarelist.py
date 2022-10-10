def squareslist():
    squares = []
    for i in range( 1, 26 ):
        squares.append( i*i )
    return squares

s1 = squareslist()
print( s1 )

s1 = [ x*x for x in range( 1, 26 ) ]
print( s1 )

s1 = [ x*x for x in range( 1, 26 ) if x%10 != 5]
print( s1 )
