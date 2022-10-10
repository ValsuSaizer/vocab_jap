from random import randint
from copy import deepcopy

color = [ "Hearts", "Spades", "Clubs", "Diamonds" ]
value = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace" ]
deck = []

for i in color:
    for j in value:
        deck += [ i + "-" + str(j) ]

def shuffle_deck( adeck ):
    bdeck = []
    while len( adeck ) > 0:
        i = randint( 0, len( adeck ) - 1 )
        bdeck.append( adeck[i] )
        adeck.pop( i )
    for element in bdeck:
        adeck.append( element )
    return adeck

def main():
    print( deck )
    print( shuffle_deck( deck ) )

if __name__ == "__main__":
    main()
