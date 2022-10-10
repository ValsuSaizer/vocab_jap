from pcinput import getString

# This function determine the common characters by adding them in a third variable. It's initiated with two parameters.
# The third variable gets compared to avoid adding the same characters multiple time
# Then, we use the len function to get the longer of the third variable which have all similar characters in her

def commonCharacters( string1, string2 ):
    result = ""
    for x in string1:
        for y in string2:
            if x == y:
                if x in result:
                    continue
                else:
                    result += x
    if len( result ) == 1:
        return "The two words only have 1 character in common"
    return "The two words have {} common characters".format( len( result ) )

word1 = getString( "Please enter a first word: " )
word2 = getString( "Please enter a second word: " )
print( commonCharacters( word1, word2 ) )
