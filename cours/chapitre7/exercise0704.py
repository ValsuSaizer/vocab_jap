bottles = 99
while bottles > 0:
    print( "{} bottles of beer on the wall, {} bottles of beer. Take one down, pass it around, {} bootes of beer on the wall.".format( bottles, bottles, bottles - 1 ) )
    bottles -= 1
