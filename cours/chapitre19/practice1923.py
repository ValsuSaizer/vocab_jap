pwr = 1
num = 75
for p in range( 0, 8 ):
    if pwr == 128:
        num = num | pwr
    pwr = pwr<<1
print( num )
