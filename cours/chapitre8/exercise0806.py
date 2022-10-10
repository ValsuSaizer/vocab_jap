from pcinput import getInteger

def factorial( x ):
    result = x
    for i in range( 1, x ):
        result = result * ( x - 1 )
        x -= 1
    return result

def binomialCoef( prompt1, prompt2 ):
    while True:
        n = getInteger( prompt1 )
        k = getInteger( prompt2 )
        if n < k:
            print( "n must be bigger than or equal to k." )
            continue
        break
    binomCoef = factorial( n ) / ( factorial( k ) * factorial( n - k ) )
    return int( binomCoef )

def main():
    num1 = "Enter a value for n: "
    num2 = "Enter a value for k: "
    print( "The binomial coefficient of n and k is {}.".format(binomialCoef ( num1, num2 ) ) )

if __name__ == "__main__":
    main()
