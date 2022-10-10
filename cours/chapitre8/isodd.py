from pcinput import getInteger

def isEven( x ):
    if x % 2 == 0:
        return True
    else:
        return False

def isOdd( y ):
    if isEven( y ):
        return "The number is even."
    else:
        return "The number is odd."


print( isOdd( 9 ) )

print( isOdd( 8 ) )
