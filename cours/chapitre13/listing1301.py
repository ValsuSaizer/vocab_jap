fruitbasket = { "apple":3, "banana":5, "cherry":50 }
for key in fruitbasket:
    print( "{}:{}".format( key, fruitbasket[key] ) )

fruitbasket["mango"] = 1
print( fruitbasket )
fruitbasket["mango"] = 6
print( fruitbasket )
print( len( fruitbasket ) )

