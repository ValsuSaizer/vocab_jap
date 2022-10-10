def toh( pole_st, pole_tmp, pole_to, size ):
    if size == 1:
        print( "move disc 1 from", pole_st, "to", pole_to )
        return 1
    moves = toh( pole_st, pole_to, pole_tmp, size-1 )
    print( "move disc", size, "from", pole_st, "to", pole_to )
    moves += 1 + toh( pole_tmp, pole_st, pole_to, size-1 )
    return moves
    
def main():
    print( toh( "A", "B", "C", 4 ) )

if __name__ == '__main__':
    main()


