sentence = "as it. turned out our chance meeting with REverend \
aRTHUR BElling was was to change our whole way of life, and \
every sunday we'd hurry along to St lOONY up the Crean BUn \
and Jam..."
arranged = ""
output = ""
wordlist2 = []

#2
for ch in sentence:
    if ord( ch ) >= 33 and ord( ch ) <= 64:
        arranged += " " + ch
        continue
    arranged += ch
print( arranged )
wordlist1 = arranged.split()
print( wordlist1 )

for word in range( 0, len( wordlist1 ) ):
    if wordlist1( word ) == wordlist1( word-1 ):
        continue
#5
    if word in ( monday, thuesday, wednesday, thursday, friday, saturday, sunday ):
        list2 += word[0].upper() + word[1:].lower()
        continue
    wordlist2 += word
"""
for word in wordlist:
    if word-1 == word:
        for ch in word:
            output = ""


#1
for ch in range( 0, len( sentence ) ):
    if ord( sentence[ch] ) >= 65 or ord( sentence[ch] ) <= 90:
        if ord( sentence[ch-1] ) >= 65 and ord( sentence[ch-1] ) <= 90 and ord( sentence[ch+1] ) >= 97 and ord( sentence[ch+1] ) <= 122:
            output += sentence[ch].lower()
            continue
            
    
#3
    if ch == 0:
        output += sentence[ch].upper()
        continue
    if sentence[ch-1] == " " and sentence[ch-2] == ".":
        output += sentence[ch].upper()
        continue




    output += sentence[ch]

"""

print( wordlist2 )
