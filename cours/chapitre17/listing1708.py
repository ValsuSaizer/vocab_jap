try:
    print( int( "NotAnInteger" ) )
except ValueError:
    print( "okidoki" )
#except ValueError as ex:
#    print( ex.args )
