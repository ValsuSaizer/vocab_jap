for i in range( 4 ):
    for j in range( 4 ):
        if i == j:
            continue
        else:
            print( "({},{})".format( i, j ) )
