text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

for ch in text:
    if ord( ch ) >= 33 and ord( ch ) <= 64:
       text = text.replace( ch, " " )

count = 0
wordlist = text.split()
for word in wordlist:
    if word == "wood":
        count += 1

print( "There are {} occurences of the word 'wood' in the text".format( count ) )
