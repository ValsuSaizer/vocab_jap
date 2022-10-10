a_string = input( "Please enter a string: " )
vowels = 0
if "a" in a_string or "A" in a_string:
    vowels += 1
if "e" in a_string or "E" in a_string:
    vowels += 1
if "i" in a_string or "I" in a_string:
    vowels += 1
    print( vowels )
if "o" in a_string or "O" in a_string:
    vowels += 1
if "u" in a_string or "U" in a_string:
    vowels += 1

if  vowels == 1:
    print( "There is only 1 vowel in this string." )
else:
    print( "There is ", vowels, " different vowels in this string" )
