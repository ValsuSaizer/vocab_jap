set1 = set( [ x for x in range(2, 1000 ) if x%3 == 0 ] )
print( "set1 =", set1 )
set2 = set( [ x for x in range(2, 1000 ) if x%7 == 0 ] )
print( "set2 =", set2 )
set3 = set( [ x for x in range(2, 1000 ) if x%11 == 0 ] )
print( "set3 =", set3 )
# a) divisible by 3, 7 and 11
set4 = set1 & set2 & set3 
print( "set4 =", set4 )
# b) divisible by 3 and 7 but not by 11
set5 = ( set1 & set2 ) - set3
print( "set5 =", set5 )
set6 = set( [ x for x in range(2, 1000 ) ] ) - set1 - set2 - set3
print( "set6 =", set6 )


