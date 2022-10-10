from copy import deepcopy

fruitbasket = { "apple":3, "banana":5, "cherry":50 }
fruitbasketalias = fruitbasket
fruitbasketcopy = fruitbasket.copy()
fruitbasketdeepcopy = deepcopy(fruitbasket)

print( id( fruitbasket ) )
print( id( fruitbasketalias ) )
print( id( fruitbasketcopy ) )
print( id( fruitbasketdeepcopy ) )
