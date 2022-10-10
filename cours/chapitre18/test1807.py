fp = open( "pc_binarytest.tmp", "r+b" )
#print( "1. Current position of the file pointer is", fp.tell() )
fp.seek( 50 )
#print( "2. Current position os the file pointer is", fp.tell() )
buffer = fp.read( 23 )
#print( "3. Current position of the file pointer is", fp.tell() )
#fp.close()

#print( buffer )
s = b""
for c in buffer:
    s += bytes( [ c-128 ] )
#print( "The secret words are:", s )
fp.seek( 50 )
fp.write( s )
fp.close()

fp = open( "pc_binarytest.tmp" )
while True:
    buffer = fp.readline()
    if buffer == "":
        break
    print( buffer, end="" )
fp.close()

