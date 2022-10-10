from pcinput import getInteger

board = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]

def display_board():
    print( "  |", "1 |",  "2 |", "3" )
    print( "_______________________" )
    for row in range( len( board ) ):
        print( row+1, "",  end="" ) 
        for column in range( len( board ) ):
            print( "|", board[row][column], "", end="" )
        print()

def getRowCol( player_num ):
    print( "Player", player_num, "turn." )
    while True:
        while True:
            row = getInteger( "Which row ? ")
            if row > 3 or row < 1:
                print( "The value for the row must be between 1 and 3." )
                continue
            break
        while True:    
            col = getInteger( "Which column ? ")
            if col > 3 or col < 1:
                print( "The value for the column must be between 1 and 3." )
                continue
            break
        if board[row-1][col-1] != "-":
            print( "This place is already filled, please enter another location please." )
            continue
        if player_num == 1:
            board[row-1][col-1] = "X"
            break
        board[row-1][col-1] = "O"
        break

def opponent( player_num ):
    if player_num == 1:
        return 2
    return 1

def winner( game ):
    verif = ""
    for x in game:
        for y in x:
            verif += str(y)
    for x in range( 3 ):
        if verif[x] != "-" and verif[x]==verif[x+3] and verif[x]==verif[x+6]:
            return True
    for x in range( 0, 9, 3 ):
        if verif[x] != "-" and verif[x] == verif[x+1] and verif[x]==verif[x+2]:
            return True
    if verif[0] != "-" and verif[0] == verif[4] and verif[0] == verif[8]:
        return True
    if verif[6] != "-" and verif[6] == verif[4] and verif[6] == verif[2]:
        return True
    return False
    
def main():
    player = 1
    while True:
        check_board = ""
        getRowCol( player )
        display_board()
        victory = winner( board )
        #print( victory )
        if victory == True:
            print( "Player {} wins!".format( player ) )
            break
        #check board and if the board is full, game over
        for line in board:
            for column in line:
                check_board += column
        print( check_board )
        if "-" not in check_board:
            print( "Draw game" )
            break
        player = opponent( player )
        

if __name__ == "__main__":
    main()
