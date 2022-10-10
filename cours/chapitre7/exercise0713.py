from random import randint

success = 0
TESTS = 100000
DICE = 5

for tests in range( TESTS ):
    roll = 0
    for x in range( DICE ):
        lastdice = roll
        roll = randint( 1, 6 )
        if roll < lastdice:
            break
        elif x == (DICE - 1) and roll >= lastdice:
            success += 1

print( "The probability to have each die greater than or equal to the value of the previous die with {} dies is: {}%".format( DICE, round( success / tests * 100, 4 ) ) )
