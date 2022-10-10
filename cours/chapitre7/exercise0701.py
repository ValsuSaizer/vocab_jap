from pcinput import getInteger

number = getInteger( "Please enter a number, it will gives you the multiplication table from 1 to 10: " )

for multiplicator in range( 1, 11 ):
    print( "{} * {} = {}".format( multiplicator, number, number * multiplicator ) )
