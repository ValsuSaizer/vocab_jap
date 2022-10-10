SUITS = [ "Hearts", "Spades", "Clubs", "Diamonds" ]
VALUES = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace" ]
class Card:
    def __init__( self, suit, value ):
        self.suit = suit
        self.value = value
    def __repr__( self ):
        return "{},{}".format( self.suit, self.value )
    def __str__( self ):
        return "card {} {}".format( SUITS[self.suit], VALUES[self.value] )
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

c1 = Card( 1, 10 )
c2 = Card( 3, 12 )
print( c1 )
print( c2 )
print( c1 == c2 )
print( c1 > c2 )
print( c1 >= c2 )
print( c1 < c2 )
print( c1 <= c2 )
