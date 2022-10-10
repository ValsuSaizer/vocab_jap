from pcinput import getString

word1 = getString( "Please enter a first word: ")
word2 = getString( "Please enter a second word: ")
result = ""
for letter in word1:
    if letter in word2 and letter not in result :
        result += letter

if result == "":
    print( "There is no common letters between the two words" )
else:
    print( "There are the following letters in common between the two words :", result )
