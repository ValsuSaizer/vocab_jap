from os.path import exists

if exists( "pc_rose.txt" ):
    print( "Rose exists" )
else:
    print( "Rose does not exist" )

if exists( "pc_tulip.txt" ):
    print( "Tulip exists" )
else:
    print( "Tulip does not exist" )
