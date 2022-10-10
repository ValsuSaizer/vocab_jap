def factorial( maxnum ):
    n1 = 1
    for i in range( 1, 11 ):
        n1 = n1 * i
        yield n1

seq = factorial( 10 )

for n in seq:
    print( n )
