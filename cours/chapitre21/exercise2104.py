from copy import deepcopy

class FruitBasket:
    def __init__( self, basket={} ):
        self.basket = basket
#    def __repr__( self ):
#        return "{}".format( self.basket )
    def __repr__( self ):
        s = ""
        sep = "["
        for fruit in self.basket:
            s += sep + fruit + ":" + str( self.basket[fruit] )
            sep = ", "
        s += "]"
        return s
    def __add__( self, fruit ):
        if isinstance( fruit, str ):
            self.basket[fruit] = self.basket.get( fruit, 0 ) + 1
            return self
        return NotImplemented
    def __iadd__( self, fruit ):
        if isinstance( fruit, str ):
            self.basket[fruit] = self.basket.get( fruit, 0 ) + 1
            return self
        return NotImplemented
    def __sub__( self, fruit ):
        if isinstance( fruit, str ):
            self.basket[fruit] = self.basket.get( fruit, 0 ) - 1
            if self.basket[fruit] == 0:
                del self.basket[fruit]
            return self
        return NotImplemented
    def __isub__( self, fruit ):
        if isinstance( fruit, str ):
            self.basket[fruit] = self.basket.get( fruit, 0 ) - 1
            if self.basket[fruit] == 0:
                del self.basket[fruit]
            return self
        return NotImplemented
    def __contains__( self, fruit ):
        if isinstance( fruit, str ):
            check = self.basket.get( fruit )
            if check:
                return True
            return False
        return NotImplemented
    def __getitem__( self, fruit ):
        if isinstance( fruit, str ):
            try:
                return self.basket[fruit]
            except KeyError:
                return 0
        return NotImplemented
    def __setitem__( self, fruit, q ):
        if isinstance( fruit, str ) and isinstance( q, int ):
            self.basket[fruit] = q
            if self.basket[fruit] == 0:
                del self.basket[fruit]
            return self
        return NotImplemented
    def __len__( self ):
        return len( self.basket )

bk1 = FruitBasket()
print( bk1 )
bk1 = bk1 + "apple"
print( bk1 )
bk1 = bk1 + "mango"
print( bk1 )
bk1 = bk1 + "mango"
print( bk1 )
bk1 += "mango"
bk1 += "banana"
print( bk1 )
bk1 = bk1 - "banana"
print( bk1 )
bk1 -= "mango"
print( bk1 )
print( "mango" in bk1 )
print( bk1["mango"])
print( bk1["banana"])
print( bk1[0])
bk1["strawberry"] = 4
bk1["mango"] = 6
print( bk1 )
bk1["mango"] = 0
print( bk1 )
print( len( bk1 ) )
