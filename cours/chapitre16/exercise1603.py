INPUT = "pc_woodchuck.txt"
OUTPUT = "pc_woodchuck.tmp"

def displaytextfile( filename ):
    fp = open( filename )
    buffer = fp.read()
    fp.close()
    print( buffer )

displaytextfile( INPUT )

fi = open( INPUT )
fo = open( OUTPUT, "w" )
charread = 0
charwrote = 0

while True:
    buffer = fi.readline()
    buffer = buffer.lower()
    for char in buffer:
        charread += 1
        charwrote += 1
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "y":
            buffer = buffer.replace( char, "" )
            charwrote -= 1
    if buffer == "":
        break
    fo.write( buffer )

fi.close()
fo.close()

fo = open( OUTPUT )

check = 0
checktext = fo.read()
for char in checktext:
    check += 1
fo.close() 

displaytextfile( OUTPUT )
print( charread )
print( charwrote )
print( check )
