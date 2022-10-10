from random import randint

class Point:
    def __init__( self, x=0.0, y=0.0, color=randint(0,(2**24)-1) ):
        self.x = x
        self.y = y
        self.color = color
    def __repr__( self ):
        return "({}, {}, color={})".format( self.x, self.y, self.color )

p = Point( 3.5, 5.0 )
print( p )
