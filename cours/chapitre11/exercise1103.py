def iftuple( sort ):
    for element in sort:
        if isinstance( element, tuple ): 
            iftuple( element )
        elif isinstance( element, int ):
            print( element )



def main():
    inttuple = ( 1, 2, ( 3, 4 ), 5, ( ( 6, 7, 8, ( 9, 10 ), 11 ), 12, 13 ), ( ( 14, 15, 16 ), ( 17, 18, 19, 20 ) ) )
    iftuple( inttuple )

if __name__ == "__main__":
    main()
