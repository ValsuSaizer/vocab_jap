from random import random
# Iterated Prisoner's Dilemma
COOPERATE = 'C'
DEFECT = 'D'
ROUNDS = 100

class Strategy:
    def __init__( self, name="" ):
        self.name = name
        self.score = 0
    def choice( self ):
        # Should return COOPERATE or DEFECT
        return NotImplemented
    def lastmove( self, mymove, opponentmove ):
        # Gets passed the last move made, after a call of choice()
        pass
    def incscore( self, n ):
        self.score += n

class Random( Strategy ):
    def choice( self ):
        if random() >= 0.5:
            return COOPERATE
        return DEFECT

class AlwaysDefect( Strategy ):
    def choice( self ):
        return DEFECT

class MemStrat( Strategy ):
    def __init__( self, name="" ):
        super().__init__( name )
        self.logs = []
    def lastmove( self, player, opponent ):
        self.logs.append( ( player, opponent ) )

class TitForTat( MemStrat ):
    def choice( self ):
        if len( self.logs ) == 0:
            return COOPERATE
        return self.logs[-1][1]

class TitForTwoTats( MemStrat ):
    def choice( self ):
        if len( self.logs ) < 2:
            return COOPERATE
        elif self.logs[-1][1] == self.logs[-2][1] and self.logs[-1][1] == DEFECT:
            return DEFECT
        return COOPERATE

class Majority( MemStrat ):
    def choice( self ):
        count = 0
        for x in self.logs:
            if x[1] == DEFECT:
                count += 1
        if count > len( self.logs ) / 2:
            return DEFECT
        return COOPERATE

strategy1 = Random( "number 1")
strategy2 = Majority( "number 2" )

for i in range( ROUNDS ):
    c1 = strategy1.choice()
    c2 = strategy2.choice()
    try:
        print( "{} c1,   {} c2".format( c1, c2 ) )
    except IndexError:
        print( "{} p2 current".format( strategy2.choice() ) )
        pass
    if c1 == c2:
        strategy1.incscore( 3 if c1 == COOPERATE else 1 )
        strategy2.incscore( 3 if c2 == COOPERATE else 1 )
    else:
        strategy1.incscore( 0 if c1 == COOPERATE else 6 )
        strategy2.incscore( 0 if c2 == COOPERATE else 6 )
    strategy1.lastmove( c1, c2 )
    strategy2.lastmove( c2, c1 )

print( "End score of", strategy1.name, "is", strategy1.score )
print( "End score of", strategy2.name, "is", strategy2.score )
