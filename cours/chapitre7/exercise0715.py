from pcinput import getInteger

loop = 0
coconut = 0

while True:
    pirates = getInteger( "Please indicate the number of pirates: " )
    if pirates == 0:
        print( "This program isn't conceived to run with 0 pirates!" )
        continue
    break

while coconut < 1000000:
    coconut += 1
    print( coconut )
    if coconut%pirates == 1 and coconut//pirates >= 1:
        remain = coconut
        for x in range( pirates + 1 ):
            if remain%pirates == 1 and remain//pirates >= 1:
                remain -= 1
                remain -= remain/pirates
            else:
                break
            if x == pirates:
                print(coconut)
                print( "To achieve this for {} pirates, you need {} coconuts.".format( pirates, coconut ) )
                print( int( remain ) )
                exit()
                
