fp = open( "pc_rose.txt" )
while True:
    parcour = fp.readline()
    buffer = parcour
    #print( type( buffer ) )
    for chara in buffer:
        #print( ord( chara ) )
        if ord( chara ) >= 65 and ord( chara ) <= 90:
            continue
        elif ord( chara ) >= 97 and ord( chara ) <= 122:
            continue
        elif ord( chara ) == 32:
            continue
        buffer = buffer.replace( chara, "" )
    verif = buffer.split()
    #print( "verif=", verif )
    for word in verif:
        if word == "name":
            print( parcour )
    if buffer == "":
        break
fp.close()
