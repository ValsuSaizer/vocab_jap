import math

a = float( input( "Please enter the length of one triangle side: " ) )
b = float( input( "Please enter the length of the second triangle side! ") )
c = math.sqrt( pow( a, 2 ) + pow( b, 2 ) )
result = "The length of the diagonale side is {:.2f} while the two sides are {:.2f} and {:.2f}"
print( result.format( c, a, b ) )
