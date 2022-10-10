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
    def get_surface_area( self ):
        return "surface area={}".format( self.width*self.height )
    def get_circumference( self ):
        return "circumference={}".format( (self.width+self.height)*2 ) 
    def get_bottom_right( self ):
        return Point( self.point.x + self.width, self.point.y - self.height )         
    def overlaping( self, rectangle ):
        #take in account cases where r1 is in front of r2
        r1, r2 = self, rectangle
        if self.point.x > rectangle.point.x:
            r1, r2 = rectangle, self
        #take in account if r1 is below r2
        if r1.point.y < r2.point.y:
            r3 = Rectangle( Point( r2.point.x, r1.point.y ), (r1.point.x + r1.width) - ( r2.get_bottom_right().x - r2.width ), ( r1.get_bottom_right().y + r1.height ) - ( r2.point.y - r2.height ) )
        else:
            r3 = Rectangle( r2.point, abs( r1.get_bottom_right().x - r2.point.x ), abs( r1.get_bottom_right().y - r2.point.y ) )
        return r3

# case if r1 is under r2
#r = Rectangle( Point( 0,3 ), 3.0, 2.0 )
#r2 = Rectangle( Point( -3,2 ), 5.0, 3.0 )

# case if r2 is under r1 and after r1
#r = Rectangle( Point( -2,3 ), 5.0, 4.0 )
#r2 = Rectangle( Point( -1,1 ), 5.0, 3.0 )

# case if r1 and r2 are superposed
r = Rectangle( Point( -2,3 ), 5.0, 4.0 )
r2 = Rectangle( Point( -2,3 ), 8.0, 6.0 )



print( r )
print( r.get_surface_area() )
print( r.get_circumference() )
print( r.get_bottom_right() )
print( "blablabla", r.overlaping( r2 ) )
print( r2 )
print( r2.get_surface_area() )
print( r2.get_circumference() )
