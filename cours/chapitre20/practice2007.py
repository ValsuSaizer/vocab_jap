from math import sqrt

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def translate( self, shift_x, shift_y ):
        self.x += shift_x
        self.y += shift_y
    def opposite( self ):
        self.x = -self.x
        self.y = -self.y

p = Point( 3.5, 5.0 )
print( p )
p.translate( -4, 7 )
print( p )
p.opposite()
print( p )
