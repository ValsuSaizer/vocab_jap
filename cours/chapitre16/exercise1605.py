from os import getcwd
from os.path import join
from copy import deepcopy

def displaycsv( csv ):
    fp = open( csv )
    while True:
        buffer = fp.readline()
        if buffer == "":
            break
        print( buffer, end="" )
    fp.close()


CSV = join( getcwd(), "exercise1605.csv" )

FILES = [ "pc_woodchuck.txt", "pc_jabberwocky.txt", "pc_rose.txt" ]

fractions = []
for file in FILES:
    fractions.append( 0 )

print( fractions )

csvdict = {}

for name in FILES:
    filename = join( getcwd(), name )
    fi = open( filename )
    fo = open( CSV, "w" )
    totalletters = 0
    while True:
        buffer = fi.readline().lower()
        if buffer == "":
            break
        for ch in buffer:
            if ord( ch ) >= 97 and ord( ch ) < 123:
                totalletters += 1
            for i in range( 97, 123 ):
                check = csvdict.get( chr( i ) )
                if check == None:
                    csvdict[chr(i)] = deepcopy( fractions )
                    csvdict[chr(i)][FILES.index( name )] = 0
                if chr( i ) == ch:
                    print( ch )
                    csvdict[chr(i)][FILES.index( name )] += 1
    for entry in csvdict:
        csvdict[entry][FILES.index( name )] = round( csvdict[entry][FILES.index( name )] / totalletters, 5 )
    print( totalletters )


fo.write( "letter" )
for name in FILES:
    fo.write( "," + name )
fo.write( "\n" )
keylist = list( csvdict.keys() )
keylist.sort()
for entry in keylist:
    fo.write( entry )
    for values in csvdict[entry]:
        fo.write( "," + str( values ) )
    fo.write( "\n" )
fi.close()
fo.close()

#displaycsv( CSV )
