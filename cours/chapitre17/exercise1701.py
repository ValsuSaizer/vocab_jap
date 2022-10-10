numlist = [ 100, 101, 0, "103", 104 ]

try:
    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except IndexError:
    print( "Pas d'index correspondant" )
except ValueError:
    print( "Vous avez saisie tout sauf un int n'est-ce-pas ?" )
except TypeError:
    print( "String de String" )
except ZeroDivisionError:
    print( "LE VIDE : IMPOSSIBLE DE DIVISER PAR 0" )
except:
    print( "sprrrrrrrrrttttttttt" )
    raise
