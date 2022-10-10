fp = open( "pc_rose.txt")
fd = open( "pc_writetest.tmp", "w" )

buffer = fp.readlines()
fd.writelines( buffer )

fp.close()
fd.close()

