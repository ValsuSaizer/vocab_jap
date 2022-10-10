fruitlist = ["apple", "banana", "cherry"]
try:
    num = input( "Please enter a number: " )
    if "." in num:
        num = float( num )
    else:
        num = int( num )
    print( fruitlist[num] )
except ValueError:
    print( "You tried something else than integer or float, right ?" )
except IndexError:
    print( "Nothing in the list with this index." )
except TypeError:
    print( "This isn't the way to call the list index." )
#except:
#    print( "Something went wrong" )
