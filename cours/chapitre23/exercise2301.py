from pcinput import getInteger

class Sequence:
    def __init__( self ):
        self.seq = list( range( 1, 101 ) )
    def __iter__( self ):
        return self
    def __next__( self ):
        if len( self.seq ) > 0:
            return self.seq.pop(0)
        raise StopIteration()
    def process( self, num ):
        i = 0
        while i < len( self.seq ):
            if self.seq[i] % num == 0:
                del self.seq[i]
                print( self.seq )
                i = 0
                continue
            i += 1

test = Sequence()

while True:
    x = getInteger( "Please enter a positive integer, to end it, enter 0: ")
    if x == 0:
        break
    if x < 0:
        print( "Incorrect value, it must be a positive integer." )
        continue
    test.process( x )

print( "Here's the list of number which aren't divisible by the input list" )
for n in test.seq:
    print( n )
