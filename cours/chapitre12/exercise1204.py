astring = "Tazmania bdgldgndghklgrsklesklblarg34fdh3d4hhdr3 !"
alphabet = "abcdefghijklmnopqrstuvwxyz"
astring = astring.lower()
letter_count = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
result = []
count = len( astring )

for i in astring:
    for j in alphabet:
        if i == j:
            letter_count[ ord( i ) - 97 ] += 1

for indice in alphabet:
    letter_count[ ord( indice ) - 97 ] = indice + "=" + str( letter_count[ ord(indice) - 97 ] )

while count >= 0:
    for element in letter_count:
        for letter in element:
            if letter == str( count ):
                result.append( element )
    count -= 1

print( result )


        

