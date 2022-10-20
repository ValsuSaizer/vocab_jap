from random import randint
from csv import reader,writer
from os import listdir

class VocSheet:
    def __init__( self ):
        self.path = path
        self.title = title
#        self.content = content
    def __repr__( self ):
        return "{}".format( self.path )
#    def showContent():

sheet = VocSheet(