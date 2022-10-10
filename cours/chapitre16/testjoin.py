from os import listdir, getcwd
from os.path import join

filelist = listdir( "." )
test = getcwd()
#print( filelist )
#print()
#print( test )
#print()
for name in filelist:
    pathname = join( getcwd(), name )
    print( pathname )
