from pcinput import getInteger

def printx():
    x = print( "x" )

def multiplex():
    integer1 = getInteger( "Please enter an integer: " )
    for i in range( integer1 ):
        printx()
    else:
        return -1

multiplex()
