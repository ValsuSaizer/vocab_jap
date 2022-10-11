from random import randint
from csv import reader,writer
from os import listdir

#Fonction de sélection aléatoire
def RandWord( words )
randindex = randint( 0, len( words ) - 1 )
    while True:
        saisie = input( "Quel est le japonais pour : " + words[randindex][0] + "\n" )
        if saisie == "exit":
            exit()
        elif saisie == "list":
            for x in words:
                print( x[0] )
            continue
        elif saisie == "menu":
            return 


#Premier prompt avec le premier choix et boucle try pour les exceptions.
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

####Mode numero 1 : une seule fiche de vocabulaire
if choice == 1:
    folder = listdir( "./fiches" )
    print( "Voici les fiches disponible." )
    for x in folder:
        print( "{} - {}".format( folder.index(x) + 1, x ) )
    while True:
        try:
            choice = int( input( "Choix: " ) )
        except ValueError:
            print( "Hey, ce n'est pas un choix valide." )
            continue
        if choice not in range(1, len( folder ) + 1 ):
            print( "Ayonyonyon... essaie une des valeurs proposées s'il te plait    ." )
            continue
        break
    sheet = "./fiches/" + folder[choice-1]
    print( sheet )
    
#Ouverture de la fiche de vocabulaire avec la boucle.
    fp = open( sheet, newline='' )
    csvreader = reader( fp )
    #print( len( csvreader ) )
    words = list( csvreader )
    while True:
        randindex = randint( 0, len( words ) - 1 )
        saisie = input( "Quel est le japonais pour : " + words[randindex][0] + "\n" )
        if saisie == "exit":
            break
        elif saisie == "list":
            for x in words:
                print( x[0] )
        continue
    fp.close()
    
####Mode 2 : toutes les fiches à la fois
elif choice == 2:
    words = []
    folder = listdir( "./fiches" )
    for entry in folder:
        fp = open( "./fiches/" + entry, newline='' )
        csvreader = reader( fp )
        for line in csvreader:
            words.append( line )
        fp.close()
        
#Sélection au hasard dans la liste de mots
    while True:
        randindex = randint( 0, len( words ) - 1 )
        saisie = input( "Quel est le japonais pour : " + words[randindex][0] + "\n" )
        if saisie == "exit":
            break
        elif saisie == "list":
            for x in words:
                print( x[0] )
        continue       

####Mode 3 : Sélection de fiche de vocabulaire
#elif choice == 3:
    


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
