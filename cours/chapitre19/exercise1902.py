from pcinput import getInteger

#def coding( inte, boo, num )


def convertbits( inte, booloo, num ): 
    if booloo == True:
        inte += ( 1 << num )
        return inte
    inte -= ( 1 << num )
    return inte

def checkbits( inte, num ):
    test = (2**num) & inte
    if test == 2**num:
        return True
    return False

def displaybits( inte, num ):
    bitstring = ""
    x = 0
    while True:
        if inte < (2**x):
            break
        check = checkbits( inte, x )
        if check == True:
            bitstring = "1" + bitstring
        else:
            bitstring = "0" + bitstring
        x += 1
    print( bitstring )

def main():
#first, main program asks for bits to add in integer
    intege = 0
    while True:
#second, asks for boolean to add or remove bits in integer
        while True:
            try:
                boolinput = int( input( "Please enter a value for bool ( 0 to remove bit, 1 to add bit ): " ) )
            except ValueError:
                print( "Please put a correct value." )
                continue
            #print( boolinput, type(boolinput ) )
            if boolinput not in range( 0, 2 ):
                print( "Please enter 0 or 1 as input for bool" )
                continue
            break

#third, asks for num value
        num = getInteger( "Please enter a number to be added to integer bits: " )
#forth, execute functions
        intege = convertbits( intege, boolinput, num ) 
        displaybits( intege, num )

#asks user if he wants to continue
        while True:
            tocontinue = input( "Do you want to continue ? ( Y or N ): " )
            if tocontinue != "Y" and tocontinue != "N":
                print( "Incorrect value, please try again." )
                continue
            break
        if tocontinue == "Y":
            continue
        print( "end" )
        break

if __name__=='__main__':
    main()
