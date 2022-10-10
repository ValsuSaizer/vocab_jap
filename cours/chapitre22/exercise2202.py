from math import pi

class Shape:
    def area( self ):
        return NotImplemented
    def circumference( self ):
        return NotImplemented

class Rectangle( Shape ):
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

class Circle( Shape ):
    def __init__( self, x, y, r ):
        self.x, self.y, self.r = x, y, r
    def __repr__( self ):
        return "[({},{}),r={}]".format( self.x, self.y, self.r )
    def area( self ):
        return pi*(r*r)
    def circumference( self ):
        return 2*pi*r


r1 = Rectangle( 2, 3, 4, 8 )
s1 = Square( 2, 3, 4 )
c1 = Circle( 2, 3, 6 )
print( s1)
print( r1 )
print( c1 )
