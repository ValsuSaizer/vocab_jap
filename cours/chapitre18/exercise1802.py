EXPRESSION = "Hello, world!"
MOST_USED = "etaoinshrdlcum "
halfbytes = []

for c in EXPRESSION:
    #forming the halfbytes list for chars in most used
    if c in MOST_USED:
        halfbytes.append( MOST_USED.find( c ) + 1 )
    #for chars outside of most used
    else:
        halfbytes.append( 0 )
        deci_val = ord( c )
        halfbytes.append( deci_val // 16 ) 
        halfbytes.append( deci_val % 16 )
if len( halfbytes ) % 2 != 0:
    halfbytes.append( 0 )
print( halfbytes )
#Conversion into decimals for bytes function
for n in range( 0, len( halfbytes ) + 1 ):
    try:
        halfbytes[n] = (halfbytes[ n ] * 16) + halfbytes[ n + 1 ]
        halfbytes.pop( n + 1 )
    except IndexError:
        continue
#Conversion into bytes
byteslist = bytes( halfbytes )
print( byteslist )
