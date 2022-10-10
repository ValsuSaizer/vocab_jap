def complexOp( complex1, complex2 ):
    complexSum = str(complex1[0] + complex2[0]) + " + " + str(complex1[1] + complex2[1]) + "i"
    complex1 = "(" + str(complex1[0]) + " + " + str(complex1[1]) + "i)"
    complex2 = "(" + str(complex2[0]) + " + " + str(complex2[1]) + "i)"
    result = complex1 + " + " + complex2 + " = " + complexSum
    return result
    



def main():
    factor1 = (6,8)
    factor2 = (2,7)
    print( complexOp( factor1, factor2 ) )

if __name__ == "__main__":
    main()
