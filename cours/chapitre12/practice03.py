from pcinput import getString

def countLetters( phrase ):
    countlist = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phrase = phrase.lower()
    for letter in phrase:
        for indice in alphabet:
            if indice == letter:
                countlist[ ord( indice ) - 97 ] += 1
    for indice in alphabet:
        countlist[ ord( indice ) - 97 ] = indice + "=" + str( countlist[ ord( indice ) - 97 ] )
    return countlist

def main():
    astring = getString( "Please enter a string: " )
    print( countLetters( astring ) )

if __name__ == '__main__':
    main()
