class Quaternion:
    def __init__( self, a, b, c, d ):
        self.a, self.b, self.c, self.d = a, b, c, d
    def __repr__( self ):
        return "({}, {}i, {}j, {}k)".format( self.a, self.b, self.c, self.d )
    def __add__( self, n ):
        if isinstance( n, int ) or isinstance( n, float ):
            return Quaternion( n+self.a, self.b, self.c, self.d )
        elif isinstance( n, Quaternion ):
            return Quaternion( n.a + self.a, n.b + self.b, \
                n.c + self.c, n.d + self.d )
        return NotImplemented
    def __radd__( self, n ):
        return self.__add__( n )
    def __sub__( self, n ):
        if isinstance( n, int ) or isinstance( n, float ):
            return Quaternion( self.a-n, self.b, self.c, self.d )
        elif isinstance( n, Quaternion ):
            return Quaternion( self.a - n.a, self.b - n.b, \
                self.c -n.c, self.d - n.d )
        return NotImplemented
    def __rsub__( self, n ):
        return n - self.a

c1 = Quaternion( 3, 4, 5, 6 )
c2 = Quaternion( 3, 4, 5, 6 )

print( 10 - c1 )
print( c1 - c2 )
