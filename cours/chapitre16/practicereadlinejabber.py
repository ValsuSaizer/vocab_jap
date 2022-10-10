fp = open( "pc_jabberwocky.txt" )
count = 0
jabber = 0
while count < 10:
    parcour = fp.readline()
    buffer = parcour.lower()
    #print( type( buffer ) )
    for chara in buffer:
        #print( ord( chara ) )
        if ord( chara ) >= 97 and ord( chara ) <= 122:
            continue
        elif ord( chara ) == 32:
            continue
        buffer = buffer.replace( chara, "" )
    verif = buffer.split()
    print( "verif=", verif )
    for word in verif:
        if word == "jabberwock":
            jabber += 1
            print( parcour )
    count += 1
    #if buffer == "":
       #break
fp.close()

print( "There is {} time(s) 'jabberwock' in the {} first lines".format( jabber, count ) ) 
