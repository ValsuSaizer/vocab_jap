FILENAME = "pc_binarytest.tmp"
fp = open( FILENAME, "rb" )
buffer = fp.read()
print( buffer )
fp.close()
