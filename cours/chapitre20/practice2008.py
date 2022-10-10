class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, tl_corner, br_corner ):
        self.tl_corner = tl_corner
        self.br_corner = br_corner
    def __repr__( self ):
        return "[top left={}, bottom right={}]".format( self.tl_corner, self.br_corner )

p1 = Point( 3.5, 5.0 )
p2 = Point( 9.0, 1.5 )
r = Rectangle( p1, p2 )
print( r )
