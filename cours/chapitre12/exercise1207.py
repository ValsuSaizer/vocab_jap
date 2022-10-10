from random import randint
from random import shuffle
from random import sample

#The #before pints are for testing, put them if not testing.


grid = [ ["-","-","-","-"],  ["-","-","-","-"],  ["-","-","-","-"] ] 
player = [ ["-","-","-","-"],  ["-","-","-","-"],  ["-","-","-","-"] ] 

def display_grid( board ):
    print( "   | ", "A ", "B ", "C ", "D " )
    print( "-----------------------------" )
    for x in range( 3 ):
        print( "", x+1, "| ", end="" )
        for y in range( 4 ):
            print( "", board[x][y], "",  end="" )
        print()

def randomizer( board ):
    #positionnement aleatoire des bateaux
    ships = [ "B", "B", "B" ]
    while len( ships ) > 0:
        for x in range( 3 ):
            for y in range( 4 ):
                if len( ships ) < 1:
                    continue
                choice = randint( 0, 1 )
                if choice == 1 and board[x][y] != "B": 
                    board[x][y] = ships[0]
                    ships.pop(0)
                     
    #Controle des espacements
        #controle des egalites d'une colonne entre les lignes
    
    #print( "board after ships placement and before shuffling" )
    #print( board )
    l = 0
    while l < 4:
        if board[1][l] == "B":
            if  board[1][l] == board[0][l] or board[1][l] == board[2][l]:
                #print( "condition 1 for shuffling l={} ".format( l ) )
                #print( "board before condition 1 shuffling" )
                #print( "   ", board )
                for j in range( 3 ):
                    shuffle( board[j] )
                #print ( "board after condition 1 shuffling" )
                #print( "   ", board )
                l = 0
                continue
        l += 1                
                
    #controle des egalites dans une meme ligne
        for g in range( 3 ):
            #h aussi en range 3 pour eviter index out of range
            for h in range( 3 ) :
                for i in range( 4 ):
                    #print( "l={} g={} h={} i={}".format( l, g, h, i ) )
                    while i == h+1 and board[g][h] == "B" and board[g][i] == "B":
                        #print( "condition 2 for shuffling g={} h={} i={}".format( g, h, i ) )
                        temp = [ board[0][h], board[1][h], board[2][h] ]
                        #print("before condition 2 (vertical) shuffle", temp )
                        #print( "   ", board )
                        for t in range( 3 ):
                            board[t][h] = "-"
                        shuffle( temp )
                        for t in range( 3 ):
                            board[t][h] = temp[0]
                            temp.pop( 0 )
                            #shuffle( board[t] )
                        #print( "after condition 2 (vertical) shuffle", temp )
                        #print( "   ", board )
                        l = 0
    return board

def shoot( play1, board ):
    while True:
        aim = input( "Please enter a position on the grid to shoot at: " )
        if len( aim ) != 2 or aim[0] not in "ABCD" or aim[1] not in "123":
            print( "invalid value" )
            continue
        if board[ int( aim[1] ) - 1 ][ ord(aim[0]) - ord( "A" ) ] == "B":
            play1[ int( aim[1] ) - 1 ][ ord(aim[0]) - ord( "A" ) ] = "B"
            print( "You sunk my battleship!" )
            break
        play1[ int( aim[1] ) - 1 ][ ord(aim[0]) - ord( "A" ) ] = "X"
        print( "Miss!" )
        break

def winner( play1 ):
    count = 0
    for x in play1:
        for y in x:
            if y == "B":
                count += 1
    if count == 3:
        return True
    return False


def main():
    moves = 0
    randomizer( grid )
    display_grid( player )
    print()
    while True:
        moves += 1
        #display_grid( grid )
        shoot( player, grid )
        display_grid( player )
        print()
        victory = winner( player )
        if victory == True:
            break
    print( "You won! It tooks you {} moves to complete.".format( moves ) )

if __name__ == '__main__':
    main()
