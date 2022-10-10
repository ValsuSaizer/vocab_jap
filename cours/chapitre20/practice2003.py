class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y

p1 = Point( 1.0, 1.0 )
p2 = Point( 2.0, 2.0 )
p3 = Point( 3.0, 3.0 )
pointlist = [ ("p1",int(p1.x),int(p1.y)), ("p2", int(p2.x), int(p2.y)), ("p3", int( p3.x ), int( p3.y )) ]
print( pointlist )
