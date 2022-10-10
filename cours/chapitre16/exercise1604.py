FILE1 = "pc_woodchuck.txt"
FILE2 = "pc_jabberwocky.txt"
FILE3 = "pc_rose.txt"

def splittextfile( text ):
    text = text.split()
    return text


remove = "!?.,:;"

resultlist = []

filelist = [ FILE1, FILE2, FILE3 ]

#1 - Create temporary files for each text to convert it with simple words
for text in filelist:
    fi = open( text )
    fo = open( text[:len(text)-3] + "tmp", "w" )
    buffer = fi.read()
    buffer = buffer.lower()
    for char in buffer:
        if char == "\n":
            buffer = buffer.replace( char, " " )
        for verif in remove:
            if char == verif:
                buffer = buffer.replace( char, "" )
    fo.write( buffer )
    fi.close()
    fo.close()

#2 - Check for similar 2 letters long words
f1 = open( FILE1[:len(FILE1)-3 ] + "tmp" )
f2 = open( FILE2[:len(FILE2)-3 ] + "tmp" )
f3 = open( FILE3[:len(FILE3)-3 ] + "tmp" )

buf1 = f1.read()
buf2 = f2.read()
buf3 = f3.read()

buf1 = buf1.split()
buf2 = buf2.split()
buf3 = buf3.split()

result = []

for word1 in buf1:
    for word2 in buf2:
        for word3 in buf3:
            if word1 == word2 and word1 == word3 and len( word1 ) >= 2:
                if word1 in result:
                    continue
                result.append( word1 )

f1.close()
f2.close()
f3.close()

print( result )
