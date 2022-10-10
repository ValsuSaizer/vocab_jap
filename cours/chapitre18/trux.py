fp = open( "trux.txt", "rb" )
buffer = fp.read()
fp.close()
print( buffer )

for c in buffer:
    print( c )
    if c == "C":
        print( "ok")
