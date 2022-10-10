from random import randint
from pcinput import getInteger

random_integer = randint( 1, 1000)
guess_count = 0
user_int_prompt = 0

while user_int_prompt != random_integer:
    user_int_prompt = getInteger( "Please enter an integer: ")
    if user_int_prompt < random_integer:
        print( "Higher")
    elif user_int_prompt > random_integer:
        print( "Lower" )
    guess_count += 1

print( "You guessed it!" )
print( "You found it in {} guess.".format( guess_count ) )
