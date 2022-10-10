word = "illusionary"
vowels = "aeiou"
progress = ""
i = 0

while i < len( word ):
    progress += word[i]
    if word[i] in vowels:
        print( len(progress) - 1 )
    i += 1
