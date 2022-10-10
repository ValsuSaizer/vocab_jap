from copy import copy

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, point, width, height ):
        self.point = copy( point )
        self.width = abs( width )
        self.height = abs( height )
        if self.width == 0:
            self.width = 1
        if self.height == 0:
            self.height = 1
    def __repr__( self ):
        return "(point={}, width={}, height={})".format( self.point, self.width, self.height )
    def __eq__( self, r2 ):
        if self.width == r2.width and self.height == r2.height:
            return "The two rectangles are equals"
        return "The two rectangles aren't equals"
    def get_surface_area( self ):
        return "surface area={}".format( self.width*self.height )
    def get_circumference( self ):
        return "circumference={}".format( (self.width+self.height)*2 ) 
    def get_bottom_right( self ):
        return Point( self.point.x + self.width, self.point.y - self.height )

# case if r1 and r2 are superposed
r = Rectangle( Point( -2,3 ), 5.0, 4.0 )
r2 = Rectangle( Point( -6,9 ), 5.0, 4.0 )

print( r == r2 )
