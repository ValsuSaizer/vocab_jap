class Squares:
    def reset( self ):
        self.nr1 = 0
    def __init__( self, maxnum=10 ):
        self.maxnum = maxnum
        self.reset()
    def __iter__( self ):
        return self
    def __next__( self ):
        self.nr1 += 1
        if self.nr1 > self.maxnum:
            raise StopIteration()
        return self.nr1*self.nr1

fseq = Squares()
for n in fseq:
    print( n, end=" " )
print()
fseq.reset()
for n in fseq:
    print( n, end=" " )
print()
