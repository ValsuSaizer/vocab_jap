from pcinput import getInteger

def getFibonacci( num, depth ):
        indent = 4 * depth * " "
        print( indent, "num=",num )
        print( indent, "num-1=", num-1, "num-2=", num-2)
        if num <= 2:
            print( indent, 1 )
            return 1
        #return getFibonacci( num-1, depth+1 ) + getFibonacci( num-2, depth+1 )
        return "{}".format( getFibonacci( num-1, depth+1 ) ) + "{}".format( getFibonacci( num-2, depth+1 ) )


def main():
    print( getFibonacci( 6, 0 ) )

if __name__ == '__main__':
    main()
