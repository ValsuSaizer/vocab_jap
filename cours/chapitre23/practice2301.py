iterator = iter( ["apple", "banana", "cherry" ] )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )
print( next( iterator, "END" ) )

iterator2 = iter( ["apple", "banana", "cherry" ] )
for fruit in iterator2:
    print( fruit )
