FILENAME = "pc_rose_copy.txt"

def binDisplay( file ):
    fp = open( file, "rb" )
    buffer = fp.read()
    print( buffer )
    fp.close()

def binEncrypt( file ):
    fp = open( file, "r+b" )
    buffer = fp.read()
    fp.seek(0)
    for b in buffer:
        if b >= 128:
            fp.write( bytes( [ b - 128 ] ) )
        else:
            fp.write( bytes( [ b + 128 ] ) )
    fp.close()


binDisplay( FILENAME )
binEncrypt( FILENAME )
binDisplay( FILENAME )

