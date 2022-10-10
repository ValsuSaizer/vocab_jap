from os.path import getsize
from os import listdir

totalsize = 0
filelist = listdir( "." )
for file in filelist:
    totalsize += getsize( file )

print( totalsize )
