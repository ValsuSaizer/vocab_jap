from pcinput import getInteger

def isEven( x ):
    if x % 2 == 0:
        return "The number is even"
    else:
        return -1

print( isEven( 7 ) )
