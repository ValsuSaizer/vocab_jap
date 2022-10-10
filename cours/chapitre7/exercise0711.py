from pcinput import getInteger

num = getInteger( "Please enter an integer: " )
string = ""
y_axis = 0
scores = "----"

while y_axis <= num:
    if y_axis == 0:
        y_axis = 1
        x_axis = 1
        while x_axis <= num:
            string = string + " " + "{:2}".format( str( x_axis ) )
            scores = scores + "---"
            x_axis += 1
        print( ".", "|",  string )
        print( scores )
    else:
        x_axis = 1
        string = ""
        while x_axis <= num:
            string = string + " " + "{:2}".format( str( y_axis * x_axis ) )
            x_axis += 1
        print ( y_axis, "|",  string )
        y_axis += 1
