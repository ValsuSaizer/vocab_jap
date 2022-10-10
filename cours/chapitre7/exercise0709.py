from pcinput import getLetter

status = ""
guess_count = 0
lower = 0
higher = 1001

while status != "C":
    guess = int( ( higher + lower ) / 2 )
    guess_count += 1
    status = getLetter( "Is it {} ? Please, tell me if the number you chose is higher (H), lower(L) or if it's the right one(C): ".format( guess ) )
    if status == "H":
        print( "Let's try higher." )
        lower = guess
    elif status == "L":
        print( "Let's try lower." )
        higher = guess
    elif status not in ("C", "H", "L"):
        print( "That's not an appropriate answer, please try again." )
        continue
    print ( guess_count )

if guess_count == 1:
    print( "I've found it in 1 try! It was: {}.".format( guess ) )
else :
    print( "I've found it! Your number was: ".format( guess ) )
    print( "It took me {} guess to find your number.".format( guess_count ) )
