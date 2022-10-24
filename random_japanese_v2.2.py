from random import randint
from csv import reader,writer
from os import listdir

#Fonction du Menu de base
def menuDebut():
    print( "Bienvenu sur ce progamme d'entrainement au vocabulaire japonais !" )
    while True:
        print( "Comment souhaites-tu travailler ?\n1 - Travailler une seule fiche ?\n2 - Travailler toutes les fiches à la fois ?\n3 - Travailler une selection de fiche ?" )
        try:
            decision = int( input( "Choix: " ) )
        except ValueError:
            if decision == "exit" or decision == "":
                exit()
            print( "Hey, ce n'est pas un choix valide." )
            continue
        if decision not in range(1,4):
            print( "Ayonyonyon... essaie une des valeurs proposées s'il te plait." )
            continue
        return decision

#Fonction de sélection aléatoire
def randWord( words ):
    words_remise = words
    remise = input( "Avec ou sans remise ?" )
    while True:
        if len( words_remise ) == 0:
            print( "Tu as vu tous les mots de la liste." )
            return None
        randindex = randint( 0, len( words_remise ) - 1 )
        saisie = input( "Quel est le japonais pour : " + words_remise[randindex][0] + "\n" )
        if remise == "1":
            words_remise.pop(randindex)
        if saisie == "exit":
            exit()
        elif saisie == "list":
            for x in words:
                print( x[0] )
            continue
        elif saisie == "menu":
            return None

####Fonction principale
def main():
    while True:
        choice = menuDebut()
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
            words = []
            fp = open( sheet, newline='', encoding="latin-1" )
            csvreader = reader( fp )
            for line in csvreader:
                words.append( line )
    #print( len( csvreader ) )
            randWord( words )

####Mode 2 : toutes les fiches à la fois
        elif choice == 2:
            words = []
            folder = listdir( "./fiches" )
            for entry in folder:
                fp = open( "./fiches/" + entry, newline='', encoding="latin-1" )
                csvreader = reader( fp )
                for line in csvreader:
                    words.append( line )
                fp.close()

#Sélection au hasard dans la liste de mots
            randWord( words )

####Mode 3 : Sélection de fiche de vocabulaire
        elif choice == 3:
            words = []
            folder = listdir( "./fiches" )
            for x in folder:
                print( "{} - {}".format( folder.index(x) + 1, x ) )
            print( "Fais ta sélection de fiches, saisi 'ok' pour valider" )
            while True:
                choice = input( "Choix : " )
                if choice == "ok":
                    break
                elif int( choice ) not in range( 1, len( folder ) + 1 ):
                    print( "Ayonyonyon... essaie une des valeurs proposées s'il te plait    ." )
                    continue
                fp = open( "./fiches/" + folder[ int( choice ) - 1 ], newline='', encoding="latin-1" )
                csvreader = reader( fp )
                for line in csvreader:
                    words.append( line )
                print( words )
#Sélection au hasard dans la liste de mots
            randWord( words )

if __name__ == '__main__':
    main()
