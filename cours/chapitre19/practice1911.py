bytestring = b'10110010'
result = 0
powerator = 1
for b in range( -1, -9, -1 ):
    if int( chr( bytestring[ b ] ) ) == 1:
        result += powerator
    powerator *= 2
print( result )
    
