text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

text = text.lower()
text = text.replace( "\n", " " )

for letter in text:
    for c in range( 33, 48 ):
        if ord( letter ) == c:
            text = text.replace( letter, "" )
    for c in range( 58, 65 ):
        if ord( letter ) == c:
            text = text.replace( letter, "" )

text = text.split()

text.sort()
worddict = {}

for word in text:
    present = worddict.get( word )
    if present:
        worddict[ word ] += 1
    else:
        worddict[ word ] = 1

print( "There's the following words in the text:" )
for entry in worddict:
    print( entry, worddict[entry] )
    
