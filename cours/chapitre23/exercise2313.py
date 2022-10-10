class Number:
    def __init__( self ):
        self.seq = [ x*x for x in range( 1, 11 )]
    def __iter__( self ):
        return self
    def __next__( self ):
        return self.seq.pop(0)

seq = zip( range(1, 11), Number() )
for y in seq:
    print( y )
