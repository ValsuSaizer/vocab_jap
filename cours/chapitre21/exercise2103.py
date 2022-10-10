from random import shuffle

SUITS = [ "Hearts", "Spades", "Clubs", "Diamonds" ]
VALUES = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace" ]

class Card:
    def __init__( self, suit, value ):
        self.suit = suit
        self.value = value
    def __repr__( self ):
        return "{},{}".format( self.suit, self.value )
    def __str__( self ):
        return "{} of {}".format( VALUES[self.value], SUITS[self.suit] )
    def __eq__( self, card2 ):
        if isinstance( card2, Card ):
            return self.value == card2.value
        return NotImplemented
    def __gt__( self, card2 ):
        if isinstance( card2, Card ):
            return self.value > card2.value
        return NotImplemented
    def __ge__( self, card2 ):
        if isinstance( card2, Card ):
            return self.value >= card2.value
        return NotImplemented
    def __lt__( self, card2 ):
        if isinstance( card2, Card ):
            return self.value < card2.value
        return NotImplemented
    def __le__( self, card2 ):
        if isinstance( card2, Card ):
            return self.value <= card2.value
        return NotImplemented

class Drawpile:
    def __init__( self, pile=[] ):
        self.pile = pile
    def __repr__( self ):
        sep = ""
        s = ""
        for obj in self.pile:
            s += sep + str( obj )
            sep = ", "
        return s
    def __len__( self ):
        return len( self.pile )
    def __getitem__( self, n ):
        return self.pile[n]
    def add( self, new_card ):
        if isinstance( new_card, Card ):
            self.pile.append( new_card )
        else:
            return NotImplemented
    def draw( self ):
        if len( self.pile ) <= 0:
            return None
        return self.pile.pop( 0 )

dp1 = Drawpile( [ Card( 3, 0 ), Card( 3, 11 ), Card( 2, 5 ) ] )
dp2 = Drawpile( [ Card( 0, 2 ), Card( 0, 1 ), Card( 1, 6 ) ] )

i = 1
while len( dp1 ) > 0 and len( dp2 ) > 0:
    print( "Round {}:".format( i ) )
    print( "Deck1 : {} VS Deck2 : {}".format( dp1[0], dp2[0] ) )
    if len( dp1 ) == 0:
        break
    if len( dp2 ) == 0:
        break
    if dp1[0] > dp2[0]:
        dp1.add( dp2[0] )
        dp2.draw()
    elif dp1[0] < dp2[0]:
        dp2.add( dp1[0] )
        dp1.draw()
    elif dp1[0] == dp2[0]:
        shuffle( dp1 )
        shuffle( dp2 )
    i += 1
