from random import randint
from csv import reader,writer
from os import listdir

while True:
    choice = input( "Est-ce que tu veux réviser une fiche (1) ou toutes les fiches (2) ? " )
    if int( choice ) not in range(1,3):
        print( "Ayonyonyon... ce n'est pas un choix valide :) Recommence s'il te plait." )
        continue
    break


folder = listdir( "fiches" )
for x in folder:
    print( x )


"""
INPUT = input( "Entrer le fichier de sortie: " ) 

fp = open( INPUT, "w", newline='' )
csvwriter = writer( fp )
for x in wordlist:
    print( x )
    csvwriter.writerow( [x] )
fp.close() 

fp = open( INPUT, newline='' )
csvreader = reader( fp )
for x in csvreader:
    print( x )
fp.close()
"""
    


"""
count = 0
while True:
    count += 1
    x = randint( 0, len( wordlist ) - 1 )
    print( x )
    x = wordlist[ x ]
    print( "number:", count )
    x = input( "Quel est le japonais de '{}' :".format( x ) )
    if x == "":
        continue
"""