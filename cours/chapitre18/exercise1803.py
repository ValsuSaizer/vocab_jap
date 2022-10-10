EXPRESSION = b'\x04\x81\xbb@,\xf0wI\xba\x02\x10'
MOST_USED = "etaoinshrdlcum "
halfbytes = []
sentence = ""

exp = "\x04\x81\xbb@,\xf0wI\xba\x02\x10"
print( exp )

for c in EXPRESSION:
    #Appending the decimal values
    if c > 15:
        halfbytes.append( int(c ) // 16 )
        halfbytes.append( int( c ) % 16 )
    else:
        halfbytes.append( 0 )
        halfbytes.append( int( c ) )
#Removing 0 at the end of list after conversion
if halfbytes[ len( halfbytes ) - 1 ] == 0:
    halfbytes.pop( len( halfbytes ) - 1 )
#conversion if character present in MOST_USED or not
for n in range( 0, len( halfbytes ) ):
    try:
        if halfbytes[n] == 0:
            halfbytes[n] = (halfbytes[ n + 1 ]*16) + halfbytes[ n + 2 ]
            halfbytes.pop( n + 1 )
            halfbytes.pop( n + 1 )
            halfbytes[n] = chr( halfbytes[n] )
        elif halfbytes[n] < 16:
            halfbytes[n] = MOST_USED[ halfbytes[n] - 1 ] 
    except IndexError:
        continue
#Result string creation
for c in halfbytes:
    sentence += c
print( sentence )
