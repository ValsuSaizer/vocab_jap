from pcinput import getInteger

"""The underneath function gives the multiplication table for a number."""
"""It first asks for a number and then gives the multiplication of this number."""

def multiplication_table( x ):
    for y in range( 1, 11 ):
        print( "{} * {} = {}".format( y, x, x * y ) )


integer = getInteger( "Please enter an integer: " )
multiplication_table( integer )
