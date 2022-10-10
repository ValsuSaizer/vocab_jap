from pcinput import getFloat

grade = getFloat( "Please enter a grade from 0 to 10: " )
if grade > 10:
    print( "You like this aren't you ?" )
    exit()
elif grade == 8.5 or grade == 9 or grade == 9.5 or grade == 10:
    print( "You got an A" )
elif grade == 7.5 or grade == 8:
    print( "You got a B" )
elif grade == 6.5 or grade == 7:
    print( "You got a C" )
elif grade == 5.5 or grade == 6:
    print( "You got a D" )
elif grade == 5 or grade == 4.5 or grade == 4 or grade == 3.5 or grade == 3 or grade == 2.5 or grade == 2 or grade == 1.5 or grade == 1 or grade == 0.5 or grade == 0:
    print( "You got a F" )
else:
    print( "Please enter a correct grade!" )
