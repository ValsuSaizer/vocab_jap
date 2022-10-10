def gcd( a, b ):
    if a % b == 0:
        return b
    return gcd( b, a % b ) 

def main():
    print( gcd( 455, 462 ) )

if __name__ == '__main__':
    main()
