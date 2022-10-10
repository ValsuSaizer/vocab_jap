from pcinput import getInteger

def removeZeros( integers ):
    i = 0
    while i < len( integers ):
        if integers[i] == 0:
            integers.pop(i)
            i = 0
        else:
            i += 1
    return integers

def subsetSum( alist, blist, level ):
    result = 0
    #Sum calculation
    blist[level] = alist[level]
    for x in blist:
        result += x
    #Shimi control
    #The two possible solutions
    if result == 0:
        #print( blist )
        removeZeros( blist )
        #return "I've found a solution! alist={} blist={} and level={}".format( alist, blist, level )
        return "I've found a solution! list={}".format( blist )
    if result != 0 and blist == alist:
        return "There's no solution for this combination, list={}".format( blist )
    #activate the last factor to initiate again the process of testing each combination
    if blist[ len( alist ) - 1 ] == 0:
        #print( "condition 1", "condition =", level )
        return subsetSum( alist, blist, len( alist ) - 1 )
    #start the defalquement when you're at the end of the list
    if level == len( alist ) - 1 and blist[ level - 1 ] == 0:
        #print( "condition 2", "condition =", level )
        blist[ len( alist ) - 1 ] = 0
        return subsetSum( alist, blist, level - 1 )
    if level == len( alist ) - 1:
        #print( "condition 3", "condition =", level )
        return subsetSum( alist, blist, level - 1 )
    if blist[ level - 1 ] == 0:
        #print( "condition 5", "condition =", level )
        for x in range( 1, len( blist[level:] ) + 1 ):
            blist[-x] = 0
        return subsetSum( alist, blist, level -1 )
    #print( "condition 6", "condition =", level )
    return subsetSum( alist, blist, level -1 )



def main():
    to_check = []
    print( "This program tests if a sequence of integers from a provided list. It does not support 0." )
    print( "Please start by input a list of integers, press enter with 0 as input to start." )
    while True:
        x = getInteger( "" )
        if x == 0:
            break
        to_check.append(x)
    #to_check = [ 1, -19, 2, -9, 4, -8, 5, 7 ]
    print( "You've entered the following sequence: {}. Processing now.".format( to_check ) )
    comparison =[]
    depth = len( to_check ) - 1
    for factor in to_check:
        comparison.append( 0 )
    print( subsetSum( to_check, comparison, depth ) )

if __name__ == "__main__":
    main()
