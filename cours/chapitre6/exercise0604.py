from math import sqrt

a = float( input( "Please enter a number for 'a': " ) )
b = float( input( "Please enter a number for 'b': " ) )
c = float( input( "Please enter a number for 'c': " ) )

if ( b * b ) - 4 * a * c < 0:
    print( "There are no solutions for this equation because you can't have a square root of a negative number" )
elif ( b * b ) - 4 * a * c == 0:
    print( "There is only 1 solution to this equation: ", -b / ( 2 * a )  )
elif a == 0:
    print( "There is only 1 solution for this equation: ", -c / b )
else:
    print( "There are 2 solutions for this equation: ", ( -b + sqrt( b * b - 4 * a * c ) / 2 * a ), " and ", ( -b - sqrt( b * b - 4 * a * c ) / 2 * a ) )
