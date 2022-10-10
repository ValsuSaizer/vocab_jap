from random import randint
from csv import reader,writer
from os import listdir

print( "Bienvenu sur ce progamme d'entrainement au vocabulaire japonais !" )
while True:
    print( "Comment souhaites-tu travailler ?\n1 - Travailler une seule fiche ?\n2 - Travailler toutes les fiches à la fois ?\n3 - Travailler une selection de fiche ?" )
    try:
        choice = int( input( "Choix: " ) )
    except ValueError:
        print( "Hey, ce n'est pas un choix valide." )
        continue
    if choice not in range(1,4):
        print( "Ayonyonyon... essaie une des valeurs proposées s'il te plait." )
        continue
    break

if choice == 1:
    folder = listdir( "fiches" )
    for x in folder:
        print( x )
    choice = 
elif choice == 2:

elif choice == 3:



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
