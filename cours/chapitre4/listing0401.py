nr1 = 5
nr2 = 4
nr3 = 5
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( nr3 / (nr1 % nr2) )
nr1 = nr1 + 1
print( "nr1 = ", nr1, "nr2 = ", nr2, "nr3 = ", nr3 )
print( nr3 / (nr1 % nr2) )
"""erreur car la dernière incrémentation résulte d'une division par zéro"""
