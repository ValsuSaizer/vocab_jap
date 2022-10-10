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

s1 = Drawpile( [ \
    Card( 1, 10 ), Card( 3, 12 ), Card( 1, 3 ), Card( 2, 5 ), Card( 0, 8 ) \
    ] )
print( s1 )
#print( len( s1 ) )
#print( s1[3] )
#s1.add( Card( 3, 5 ) )
#print( "after add", s1 )
s1.draw()
#print( s1 )
