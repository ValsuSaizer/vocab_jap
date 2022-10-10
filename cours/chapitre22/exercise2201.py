class Rectangle:
    def __init__( self, x, y, w, h ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def __repr__( self ):
        return "[({},{}), w={},h={}]".format( self.x, self.y, self.w, self.h )
    def area( self ):
        return self.w * self.h
    def circumference( self ):
        return 2*(self.w + self.h )

class Square( Rectangle ):
    def __init__( self, x, y, w ):
        super().__init__( x, y, w, w )


r1 = Rectangle( 2, 3, 4, 8 )
c1 = Square( 2, 3, 4 )
print( c1)
print( r1 )
