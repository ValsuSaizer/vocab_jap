for A in range( 1, 10):
    for B in range( 10 ):
        if B == A:
            continue
        for C in range( 10 ):
            if C == B or C == A:
                continue
            for D in range( 10 ):
                if D == C or D == B or D == A:
                    continue
                if int( str(D) + str(C) + str(B) + str(A) ) == 4 * int( str(A) + str(B) + str(C) + str(D) ):
                    print( "A={}, B={}, C={} and D={}".format( A, B, C, D ) )
                    continue
