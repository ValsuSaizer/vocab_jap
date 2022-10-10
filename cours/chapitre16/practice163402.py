fp = open( "pc_rose.txt")
fd = open( "pc_writetest.tmp", "w" )

buffer = fp.readlines()
buffer = buffer[::-1]

fd.writelines( buffer )

fp.close()
fd.close()

