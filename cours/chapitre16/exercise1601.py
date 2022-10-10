fp = open( "pc_woodchuck.txt" )
buffer = fp.read()
fp.close()

buffer = buffer.lower()
for char in buffer:
    if ord( char ) >= 97 and ord( char ) <= 122:
        continue
    if ord( char ) == 32:
        continue
    if ord( char ) == 10:
        buffer = buffer.replace( char, " " )
    else:
        buffer = buffer.replace( char, "" )

#print( buffer )

buffer = buffer.split()
buffer.sort()

#print( buffer )

dictionnary = {}
for element in buffer:
    if dictionnary.get( element ):
        dictionnary[ element ] += 1
    else:
        dictionnary[ element ] = 1

#print( dictionnary )

print( "Here's the different words with their quantities in the text file" )
for entry in dictionnary:
    print( "{} : {}".format( entry, dictionnary[ entry ] ) )
