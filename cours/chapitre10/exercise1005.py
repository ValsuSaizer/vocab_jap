string = "Hello, world!"
output = ""

for char_ascii in range( 32, 127 ):
    for ch in string:
        if char_ascii == ord( ch ):
            output += ch

print( output )
