CAPS_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ch = 0
output = ""
print( CAPS_ALPHABET )
for ch in range( 0, len( CAPS_ALPHABET ) ):
    if ch > 12:
        print( CAPS_ALPHABET[ch+13-len(CAPS_ALPHABET)], end="" )
        continue
    print( CAPS_ALPHABET[ch+13], end="" )
print()
