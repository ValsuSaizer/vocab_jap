text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

VOWELS = "aeiou"
text = text.lower()
output = ""
for letter in VOWELS:
    temporary = 0
    for ch in text:
        if letter == ch:
            temporary += 1
    if letter == "u":
        output += letter + "=" + str( temporary )
        break
    output += letter + "=" + str( temporary ) + ","

output = output.split( "," )
print( "Here's how many of each vowel there is in the text:" )
print( output )

#See the answer program but I'm disapointed
