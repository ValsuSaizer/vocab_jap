from pcinput import getInteger

def getFibonacci( num ):
        if num == 1:
            return 1
        if num < 1:
            return 0
        if num > 1:
            return getFibonacci( num-1 ) + getFibonacci( num-2 )


def main():
    print( getFibonacci( 6 ) )

if __name__ == '__main__':
    main()
