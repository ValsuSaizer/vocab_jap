pattern = 1
num = 77
for p in range( 0, 8 ):
    if p == 2:
        pattern = ~pattern
        break
    pattern = (pattern<<1)
print( pattern )

print( num & pattern )
