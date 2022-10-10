from pcinput import getInteger

num = getInteger( "Please enter an integer: " )

"""First, the first line which begin with '.'"""
print( ". | ", end="" )
for x in range( 1, num+1 ):
    print( "{:3}".format( x ), end="" )
print()

"""Then the scores"""
print( "----", end="")
for x in range( 1, num+1 ):
    print( "---", end="" )
print()

"""Then the multiplication table"""
for x in range( 1, num+1):
    print( x, "| ", end="")
    for y in range( 1, num+1):
        print( "{:3}".format( x * y ), end="")
    print()
