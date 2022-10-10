queue = [ "blablabla", "blablipbloup", "C'est mon émission !" ]

while True:
    prompt = input( "Enter something: " )
    if prompt == "":
        break
    if prompt == "?":
        if len( queue ) == 0:
            print( "The FIFO queue is empty, please enter something to fill it" )
            continue
        print( queue[0] )
        queue.pop( 0 )
        continue
    queue.append( prompt )
