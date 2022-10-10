sentence = "as it turned out our chance meeting with REverend \
aRTHUR BElling was was to change our whole way of life, and \
every sunday we'd hurry along to St lOONY up the Crean BUn \
and Jam..."

output = ""
lastword = ""

#3
sentence = sentence[0].upper() + sentence[1:]

sentence = sentence.split()
print( sentence )

for word in sentence:
    #2
    if word == lastword:
        continue
    #1
    if word[0] == word[0].upper() and word[1] == word[1].upper() and word[2:] == word[2:].lower():
        word = word[0] + word[1:].lower()

    #4
    if word[0] == word[0].lower() and word[1:] == word[1:].upper():
        word = word[0].upper() + word[1:].lower()

    #5
    if word=="monday" or word=="tuesday" or word=="wednesday" or word=="thursday" or word=="friday" or word=="saturday" or word=="sunday":
        word = word[0].upper() + word[1:]


    output += word + " "
    lastword = word

print( output )
