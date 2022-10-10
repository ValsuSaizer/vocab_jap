class Sentence:
    def __init__( self, words ):
        self.words = words
    def __repr__( self ):
        return " ".join( self.words )
    def __len__( self ):
        return len( self.words )
    def __getitem__( self, n ):
        return self.words[n]
    def __setitem__( self, n, value ):
        self.words[n] = value
    def __contains__( self, n ):
        if n in self.words:
            return True
        return False


s = Sentence( [ "There", "is", "only", "one", "thing", "worse", "than", "being", "talked", "about", "and", "that", "is", "not", "being", "talked", "about" ] )
print( s )
print( len( s ) )
print( s[5] )
s[5] = "better"
print( s[5] )
print( s )
print( "being" in s )
