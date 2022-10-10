def onlyLetters( string ):
    output = ""
    for ch in string:
        if ch >= "a" and ch <= "z":
            output += ch
            continue
        output += " "
    return output

print( onlyLetters( "ph@t l00t" ) )
