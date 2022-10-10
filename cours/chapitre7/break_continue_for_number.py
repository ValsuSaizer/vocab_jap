total = 0
for num in ( 12, 4, 3, 33, -2, -5, 7, 0, 22, 4 ):
    if num == 0:
        break
    elif num < 0:
        continue
    else:
        total += num
print( "The total is", total )
print( "Done" )
