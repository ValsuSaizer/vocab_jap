from pcinput import getInteger

# This function gives you an approximation of pi based on Gregory Leibnitz formula which is 4 * ( 1/1 - 1/3 + 1/5 etc. ).
# It first asks you for how many times the terms must be calculated (prefer a large number like > 100 to have better result).
# The function just choose between addition and substraction by checking if the range factor is even or odd (using %2 operation).

def gregoryLeibnitz( num ):
    result = 0
    y = 1
    for i in range( num ):
        if i%2 == 0:
            result += 1 / y
        else:
            result -= 1 / y
        y += 2
    return 4 * result

number = getInteger( "Please enter how many times the terms must be calculated: " )
print( gregoryLeibnitz( number ) )
