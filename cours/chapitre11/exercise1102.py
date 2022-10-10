def multiplyComplex( i, j ):
    return i[0]*j[0] - i[1]*j[1], i[0]*j[1] + i[1]*j[0]

def convertDisplay( u ):
    return "({} + {}i)".format( u[0], u[1] )
    


def main():
    a = (5,6)
    b = (2,8)
    print( convertDisplay( a ), "+", convertDisplay( b ), "=", convertDisplay( multiplyComplex( a, b ) ) )

if __name__ == "__main__":
    main()
