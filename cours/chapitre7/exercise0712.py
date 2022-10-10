z = 1

while z <= 100:
    for x in range( 1, 101 ):
        for y in range( 1, 101):
            if z == x**2 + y**2:
                print( "{} = {}**2 + {}**2".format( z, x, y ) )
    z += 1
