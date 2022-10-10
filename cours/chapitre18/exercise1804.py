from os.path import exists, getsize
from pcinput import getString, getInteger

MOST_USED = b"etaoinshrdlcum "

def compression( EXPRESSION ):
    halfbytes = []
    for c in EXPRESSION:
        #forming the halfbytes list for chars in most used
        if c in MOST_USED:
            halfbytes.append( MOST_USED.find( c ) + 1 )
        #for chars outside of most used
        else:
            halfbytes.append( 0 )
            halfbytes.append( c // 16 )
            halfbytes.append( c % 16 )
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
    return byteslist

def decompression( EXPRESSION ):
    halfbytes = []
    sentence = b""
    for c in EXPRESSION:
        print( c , type( c ))
        #Appending the decimal values
        if c > 15:
            halfbytes.append( c // 16 )
            halfbytes.append( c % 16 )
        else:
            halfbytes.append( 0 )
            halfbytes.append( c )
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
                #halfbytes[n] = chr( halfbytes[n] )
            elif halfbytes[n] < 16:
                halfbytes[n] = MOST_USED[ halfbytes[n] - 1 ]
        except IndexError:
            continue
    #Result string creation
    for c in halfbytes:
        sentence += bytes( [c] )
    return sentence

#ask the user for input file
while True:
    inputfile = getString( "Enter a name for input file: " )
    if exists( inputfile ):
        try:
            fi = open( inputfile, "rb" )
            buffer = fi.read()
            fi.close()
        except IOError as ex:
            print( inputfile, "Cannot be processed" )
            print( "Error {} : {}".format( ex.args[0], ex.args[1] ) )
        break
    else:
        print( "The file doesn't exists, please enter a already existing file." )
        continue

#ask the user for output file
while True:
    outputfile = getString( "Enter a name for output file: " )
    if exists( outputfile ):
        print( "File already exists, please enter another name" )
        continue
    else:
        try:
            fo = open( outputfile, "wb" )
        except IOError as ex:
            print( "Cannot open output file" )
            print( "Error {} : {}".format( ex.args[0], ex.args[1] ) )
        break

#ask the user for compress or decompress
while True:
    choice = getInteger( "Please choose if you want to compress or decompress the file ( 1 = compress, 2 = decompress ). " )
    if choice not in range( 1, 3 ):
        print( "Please, choose between 1 or 2." )
        continue
    break

#execution depending of choice value
print( buffer )
if choice == 1:
    buffer = compression( buffer )
else:
    buffer = decompression( buffer )
print( buffer )

#write data in output file
try:
    fo.write( buffer )
    fo.close()
except IOError as ex:
    print( "Something went wrong with writting" )
    print( "Error {} : {}".format( ex.args[0], ex.args[1] ) )
