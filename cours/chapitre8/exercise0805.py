from pcinput import getInteger

def checkNumber( prompt ):
    while True:
        num = getInteger( prompt )
        if num < 0 or num > 1000:
            print( "The number must be between 0 and 1000." )
            continue
        return num

def main():
    while True:
        x = checkNumber( "Enter a value for first number: " )
        y = checkNumber( "Enter a value for second number: " )
        if x == 0:
            break
        if y == 0:
            break
        if x%y == 0 or y%x == 0:
            print( "Error: the numbers cannot be dividers" )
            return
        print( "Multiplication of", x, "and", y, "gives", x * y )
    print( "Goodbye!" )

if __name__ == '__main__':
    main()
