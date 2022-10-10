EXPRESSION = "Hello, world!"
MOST_USED = "etaoinshrdlcum "
HEXA = "ABCDEF"
halfbytes = []

for c in EXPRESSION:
    #forming the halfbytes list for chars in most used
    if c in MOST_USED:
        if MOST_USED.find( c ) > 8:
            halfbytes.append( HEXA[ MOST_USED.find( c ) - 9 ] )
        else:
            halfbytes.append( str( MOST_USED.find( c ) + 1 ) )
    #for chars outside of most used
    else:
        halfbytes.append( "0" )
        deci_val = ord( c )
        str_bin = ""
        #Conversion into binary
        for div in range( 8 ):
            if deci_val % 2 == 1:
                str_bin = str_bin + "1"
            else:
                str_bin = str_bin + "0" 
            deci_val = deci_val // 2
        pair1 = 0
        pair2 = 0
        #Conversion from binary to hexa
        for calc in range( 4 ):
            if str_bin[ calc ] == "1":
                pair1 += 2**calc
            if str_bin[ calc + 4 ] == "1":
                pair2 += 2**calc
        if int( pair1 ) > 9:
            pair1 = HEXA[ int( pair1 ) - 10 ]
        if int( pair2 ) > 9:
            pair2 = HEXA[ int( pair2 ) - 10 ]
        halfbytes.append( str( pair2 ) )
        halfbytes.append( str( pair1 ) )
if len( halfbytes ) % 2 != 0:
    halfbytes.append( "0" )

print( halfbytes )
#Conversion into bytes
byteslist = bytes( halfbytes )
